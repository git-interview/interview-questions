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
    <dd>Onsite</dd>
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

<script type="text/javascript" src="{{ "/assets/js/toggle-answer.js" | absolute_url }}"></script>
<a class="toggle-all-answers-button">Show all answers ▽</a>


### Crawler operation
{: .no_toc }

<ol>
    <li class="question">Describe the sequence of operations the crawler needs to perform, to produce the desired output.
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: We can use a <em>queue</em> to keep track of the page URLs to be crawled next, and a <em>worker</em> that operates as follows:
            <ol>
                <li>Retrieves a page URL from the queue.</li>
                <li>Fetches page from the server.</li>
                <li>Parses the HTML to identify URLs of outbound links.</li>
                <li>Saves outbound links to DB.</li>
                <li>Queues outbound pages for subsequent processing.</li>
            </ol>
        </div>
    </li>
    <li class="question">What data structures does the crawler need?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
    <li class="question">Sketch a block diagram for the crawler that illustrates the different systems involved.
        <span class="toggle-answer-icon">▽</span>
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
    </select>
</p>

---

### Performance metrics
{: .no_toc }

<ol>
    <li class="question">What metric can we use to benchmark the <em>speed</em> of different crawlers?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
    <li class="question">What factors (internal or external) influence this metric?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li> 
    <li class="question">What design changes could we make to improve the performance of the crawler we previously designed?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
</ol>

<p>Grade:
    <select>
        <option selected disabled hidden>Choose</option>
        <option value="excellent">Excellent</option>
        <option value="good">Good</option>
        <option value="poor">Poor</option>
        <option value="very-poor">Very poor</option>
    </select>
</p>

---

### Concurrency
{: .no_toc }

<ol>
    <li class="question">Is the crawler we previously designed capable of fetching multiple webpages in parallel?
    <span class="toggle-answer-icon">▽</span>
    <div class="answer">Answer: Here</div>
    </li>
    <li class="question">How would you extend the design to allow parallel fetching?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li> 
    <li class="question">How would you implement parallel fetching using <em>multiple processes</em>? <em>Single process</em>? <em>Single thread</em>?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
    <li class="question">How can the crawler enforce that the maximum number of distinct pages to visit is, say, <code class="highlighter-rouge">1000</code>? Are there situations where the crawler stops before reaching 1000 pages?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
    <li class="question">How can the crawler avoid crawling the same URL more than once?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
    <li class="question">How would the crawler handle query parameters in a URL?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
</ol>

<p>Grade:
    <select>
        <option selected disabled hidden>Choose</option>
        <option value="excellent">Excellent</option>
        <option value="good">Good</option>
        <option value="poor">Poor</option>
        <option value="very-poor">Very poor</option>
    </select>
</p>

---

### Robustness to errors
{: .no_toc }

<ol>
    <li class="question">What types of errors can the crawler encounter while navigating webpages?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
    <li class="question">How can we handle 4xx errors?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
    <li class="question">How can we handle 5xx errors?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
    <li class="question">How can we handle DNS errors?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
</ol>

<p>Grade:
    <select>
        <option selected disabled hidden>Choose</option>
        <option value="excellent">Excellent</option>
        <option value="good">Good</option>
        <option value="poor">Poor</option>
        <option value="very-poor">Very poor</option>
    </select>
</p>

---

### Data structures
{: .no_toc }

<ol>
    <li class="question">Where can the crawler store this data structure?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
    <li class="question">What are the tradeoffs between storing this data structure <em>in memory</em> vs. <em>in disk</em>?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
    <li class="question">How would you store this data struture in a <em>relational database</em>, such as MySQL?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
    <li class="question">How would you store this data struture in a <em>key-value database</em>, such as Redis?
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
</ol>

<p>Grade:
    <select>
        <option selected disabled hidden>Choose</option>
        <option value="excellent">Excellent</option>
        <option value="good">Good</option>
        <option value="poor">Poor</option>
        <option value="very-poor">Very poor</option>
    </select>
</p>

---

### Topic
{: .no_toc }

<ol>
    <li class="question">Question
        <span class="toggle-answer-icon">▽</span>
        <div class="answer">Answer: Here</div>
    </li>
</ol>

<p>Grade:
    <select>
        <option selected disabled hidden>Choose</option>
        <option value="excellent">Excellent</option>
        <option value="good">Good</option>
        <option value="poor">Poor</option>
        <option value="very-poor">Very poor</option>
    </select>
</p>

---


[Notify me when Interview Pro launches](/notify-me){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
[Give feedback](/give-feedback){: .btn .fs-5 .mb-4 .mb-md-0 }


© 2020 Interview Pro
{: .fs-1 .fw-300 .text-grey-dk-000}

