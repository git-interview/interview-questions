"""Solution using Python 3.

To run:
    pip install -r requirements.txt
    python solution.py
"""

import logging
import time
import traceback
import asyncio
import aiohttp
import pandas
import sys
from pyquery import PyQuery as pq
from urllib.parse import urljoin, urlparse


# configure logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)
log = logging.getLogger(__name__)


# DB
pages = pandas.DataFrame(columns=('url', 't_start', 't_end', 'http_status')).set_index('url')
links = pandas.DataFrame(columns=('from_url', 'to_url', 't')).set_index(['from_url', 'to_url'])


def save_link(from_url, to_url):
    links.loc[(from_url, to_url), ['t']] = get_current_time()


async def main():
    max_pages = 10
    nr_workers = 1

    # queue contains canonical URLs to be crawled
    queue = asyncio.Queue()
    
    # url = get_canonical_url(base='http://robinhood.com')
    url = get_canonical_url(base='http://checkr.com')
    # url = get_canonical_url(base='http://httpbin.org/get')
    queue.put_nowait(url)

    # Create worker tasks to process the queue concurrently.
    tasks = []
    for i in range(nr_workers):
        name = f'worker{i}'
        log.debug(f'[main] Creating {name}')
        task = asyncio.create_task(worker(
            name=name,
            queue=queue,
            pages=pages,
            links=links,
            max_pages=max_pages,
        ))
        tasks.append(task)

     # Wait until the queue is empty.
    await queue.join()
    log.debug(f'[main] Queue is empty, stopping workers...')

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    log.debug(f'Processed {len(pages)} pages:')
    log.debug(pages.head(20))

    # display in-degree of each page
    log.debug(f'Processed {len(links)} links:')
    log.debug(links.head(20))
    in_degree = links.groupby('to_url').count()
    in_degree.columns = ['in_degree']
    in_degree.sort_values(by='in_degree', ascending=False, inplace=True)
    log.debug(in_degree.head(20))

    pages.to_csv('pages.csv')
    links.to_csv('links.csv')
    in_degree.to_csv('in_degree.csv')


async def worker(name, queue, pages, links, max_pages):
    while True:
        log.debug(f'[{name}] ' + '-' * 100)
        log.debug(f'[{name}] len(pages) {len(pages)}')
        log.debug(f'[{name}] queue.qsize() {queue.qsize()}')

        # Get a "work item" out of the queue.
        url = await queue.get()
        log.debug(f'[{name}] Processing page {url}...')

        if len(pages) >= max_pages:
            log.debug(f'[{name}] Page limit of {max_pages} reached, skipping...')
            queue.task_done()
            continue

        if url in pages.index:
            log.debug(f'[{name}] Page is already processed, skipping...')
            queue.task_done()
            continue

        pages.loc[url] = {
            't_start': get_current_time(),
            't_end': None,
            'http_status': None,
        }

        try:
            http_status, content_type, html_body = await get_page(url=url)
        except:
            log.error(f'[{name}] Failed to get page, skipping...')
            traceback.print_exc(file=sys.stdout)
            pages.loc[url].t_end = get_current_time()
            queue.task_done()
            continue

        pages.loc[url].http_status = http_status
        pages.loc[url].content_type = content_type
        if content_type != 'text/html':


        # parse HTML body and find all URLs
        link_urls = get_outbound_links(html=html_body, base_url=url)

        # save links in DB
        for link_url in link_urls:
            save_link(from_url=url, to_url=link_url)

        # insert linked pages in queue, for later processing
        for link_url in link_urls:
            queue.put_nowait(link_url)
        
        # mark page as processed
        pages.loc[url].t_end = get_current_time()
        queue.task_done()
        log.debug(f'[{name}] Done processing links in page.')


async def get_page(url):
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=20)) as session:
        resp = await session.get(url)
        body = await resp.text()


def get_outbound_links(html, base_url):
        urls = get_urls_from_html(html=html, base_url=base_url)
        # exclude current url from links
        outbound_urls = [u for u in urls if u != url]
        return outbound_urls


def get_urls_from_html(html, base_url):
    # parse HTML body and find all URLs
    # returned urls are canonical
    canonical_urls = []
    pbody = pq(html)
    for anchor in pbody('a'):
        if 'href' in anchor.attrib:
            canonical_url = get_canonical_url(base=base_url,
                                              url=anchor.attrib['href'])
            if is_http(canonical_url=canonical_url):
                log.debug(f'Found canonical http url {canonical_url}')
                canonical_urls.append(canonical_url)
    return canonical_urls


def get_canonical_url(base, url=''):
    curl = urljoin(base=base, url=url)
    if curl.endswith('/'):
        curl = curl[:-1]
    return curl


def is_http(canonical_url):
    webpage_schemes = [
        'http',
        'https',
    ]
    parsed_url = urlparse(canonical_url)
    return (parsed_url.scheme in webpage_schemes)


def get_current_time():
    return time.time()


if __name__ == '__main__':
    asyncio.run(main())
    # asyncio.run(main(), debug=True)

