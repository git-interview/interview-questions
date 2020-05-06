---
grand_parent: "Backend"
parent: "Build a web crawler"
title: "Onsite"
nav_order: 3
layout: default
permalink: "/backend-questions/build-a-web-crawler/onsite"
---


# Onsite
{: .no_toc }

<dl>
    <dt>Task</dt>
    <dd>Design a simple web crawler and discuss tradeoffs.</dd>

    <dt>Duration</dt>
    <dd>45 mins</dd>

    <dt>Topics</dt>
    <dd>Distributed Systems, Data Structures, Concurrency</dd>

    <dt>Format</dt>
    <dd>Onsite interview</dd>
</dl>


---


#### On this page
{: .no_toc }

1. TOC
{: toc}


---


## Scenario
{: .d-inline-block }
During onsite
{: .label .label-green }


Our goal is to design and implement a simplified webcrawler. The system should accept an initial webpage to crawl, such as:

```
https://apple.com
```

from which it should progressively discover all linked pages. To limit the amount of work performed by the crawler, it should accept a maximum number of distinct pages to visit, for example, `50`.

As the crawler visits pages, it should build a general representation of how pages link to each other. Upon completion, it should print the complete list of pages visited, sorted by decreasing *in-degree* (ie, how many pages link to it). For example:

```
URL                               IN-DEGREE
---------------------------------------------
https://apple.com/us/search           44
https://www.icloud.com                42
https://support.apple.com             36
https://apple.com/us/shop             35
https://apple.com/ipad                34
https://apple.com/watch               34
https://apple.com/tv                  34
https://apple.com/music               34
https://apple.com/mac                 34
https://apple.com/iphone              34
...
```


---


## Questions
{: .d-inline-block } 
During onsite
{: .label .label-green }

<script type="text/javascript" src="{{ "/assets/js/toggle-all-answers.js" | absolute_url }}"></script>
<a class="toggle-all-answers-button">Show all answers ▽</a>


### Design

<ol>
    <li class="question-answer">
        <div class="question">Describe the sequence of operations the crawler needs to perform, to produce the desired output. What data structures are needed?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <h5>Data structures</h5>
            <p>
                <ul>
                    <li>A queue, for keeping track of the page URLs to crawl next.</li>
                    <li>A database, for keeping track of the crawled webgraph: the nodes are `pages`, and the edges are `links`.</li>
                </ul>
            </p>
            <h5>Algorithm</h5>
            <p>
                <em>Phase 1: Crawl.</em> We use a <em>queue</em> to keep track of the page URLs to crawl next, and one <em>worker</em> (or many workers, in a concurrent solution) that operates as follows:
                <ol>
                    <li>Retrieves a page URL from the queue.</li>
                    <li>Fetches page from the server.</li>
                    <li>Parses the HTML to identify URLs of outbound links.</li>
                    <li>Queues outbound links, for later crawling.</li>
                    <li>Saves outbound links to a DB, for later computing graph statistics.</li>
                </ol>
                <br>
                <em>Phase 2: Compute statistics.</em> To obtain the desired in-degree statistics, we group by destination URL, count how many pages link to each destination, and sort by decreasing count.
            </p>
        </div>
    </li>
    <li class="question-answer">
        <div class="question">Draw a block diagram for the crawler that illustrates the different systems involved.
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">Answer: Block diagram</div>
    </li>
</ol>

<p>Grade:
    <select>
        <option selected disabled hidden>Choose</option>
        <option value="excellent">Excellent</option>
        <option value="good">Good</option>
        <option value="poor">Poor</option>
        <option value="very-poor">Very poor</option>
        <option value="did-not-discuss">Did not discuss</option>
    </select>
</p>

---

### Performance

<ol>
    <li class="question-answer">
        <div class="question">What metric can we use to benchmark the <em>speed</em> of different crawlers?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
    <li class="question-answer">
        <div class="question">What factors (internal or external) influence this metric?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li> 
    <li class="question-answer">
        <div class="question">What changes can we make to the previous design to improve the crawler's performance?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
</ol>

<p>Grade:
    <select>
        <option selected disabled hidden>Choose</option>
        <option value="excellent">Excellent</option>
        <option value="good">Good</option>
        <option value="poor">Poor</option>
        <option value="very-poor">Very poor</option>
        <option value="did-not-discuss">Did not discuss</option>
    </select>
</p>

---

### Concurrency

<ol>
    <li class="question-answer">
        <div class="question">Is the crawler we previously designed capable of fetching multiple webpages simultaneously? Why is such capability important?
        <span class="toggle-answer-icon">▽</span>
    </div>
    <div class="answer">
        <h4>Answer</h4>
        <p>Here</p>
    </div>
    </li>
    <li class="question-answer">
        <div class="question">How would you extend the design to enable parallel fetching? Can this be accomplished using a single thread of execution?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li> 
    <li class="question-answer">
        <div class="question">How can the crawler avoid fetching the same URL more than once? Is the proposed mechanism free from race conditions?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
    <li class="question-answer">
        <div class="question">How can the crawler enforce that the maximum number of distinct pages to visit is, say, <code>50</code>? Is the proposed mechanism free from race conditions? Are there situations where the crawler stops before reaching the limit of <code>50</code> pages?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
</ol>

<p>Grade:
    <select>
        <option selected disabled hidden>Choose</option>
        <option value="excellent">Excellent</option>
        <option value="good">Good</option>
        <option value="poor">Poor</option>
        <option value="very-poor">Very poor</option>
        <option value="did-not-discuss">Did not discuss</option>
    </select>
</p>

---

### Robustness

<ol>
    <li class="question-answer">
        <div class="question">What types of errors can the crawler encounter while processing webpages?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
    <li class="question-answer">
        <div class="question">How can the crawler handle rate limiting by servers? How would you modify the previous design to support this functionality?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
    <li class="question-answer">
        <div class="question">How can the crawler handle <code>4xx</code> errors? How about <code>5xx</code> errors? How about DNS resolution errors?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
    <li class="question-answer">
        <div class="question">How can the crawler handle query parameters in a URL, such as <code>https://www.apple.com?view=false</code>?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
</ol>

<p>Grade:
    <select>
        <option selected disabled hidden>Choose</option>
        <option value="excellent">Excellent</option>
        <option value="good">Good</option>
        <option value="poor">Poor</option>
        <option value="very-poor">Very poor</option>
        <option value="did-not-discuss">Did not discuss</option>
    </select>
</p>

---

### Storage

<ol>
    <li class="question-answer">
        <div class="question">As the crawler visits pages, it builds a representation of how pages link to each other. Where can the crawler store this data structure?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
    <li class="question-answer">
        <div class="question">What are the tradeoffs between storing this data structure <em>in memory</em> vs. <em>in disk</em>?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
    <li class="question-answer">
        <div class="question">How would you store this data struture in a <em>relational database</em>, such as MySQL?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
    <li class="question-answer">
        <div class="question">How would you store this data struture in a <em>key-value database</em>, such as Redis?
            <span class="toggle-answer-icon">▽</span>
        </div>
        <div class="answer">
            <h4>Answer</h4>
            <p>Here</p>
        </div>
    </li>
</ol>

<p>Grade:
    <select>
        <option selected disabled hidden>Choose</option>
        <option value="excellent">Excellent</option>
        <option value="good">Good</option>
        <option value="poor">Poor</option>
        <option value="very-poor">Very poor</option>
        <option value="did-not-discuss">Did not discuss</option>
    </select>
</p>

---


[Notify me when Interview Pro launches](/notify-me){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
[Give feedback](/give-feedback){: .btn .fs-5 .mb-4 .mb-md-0 }


© 2020 Interview Pro
{: .fs-1 .fw-300 .text-grey-dk-000}

