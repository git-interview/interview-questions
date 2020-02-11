---
grand_parent: "Backend"
parent: "Build a web crawler"
title: "Take-home"
nav_order: 2
layout: default
permalink: "/backend-questions/build-a-web-crawler/take-home"
---


# Take-home
{: .no_toc }

<dl>
    <dt>Task</dt>
    <dd>Design and implement a simple web crawler.</dd>

    <dt>Duration</dt>
    <dd>2 hours</dd>

    <dt>Difficulty</dt>
    <dd>Medium</dd>

    <dt>Topics</dt>
    <dd>Distributed Systems</dd>

    <dt>Format</dt>
    <dd>Take-home</dd>
</dl>


--- 


1. TOC
{: toc}


---


## Problem statement
{: .d-inline-block } 
For candidate 
{: .label .label-green }


Our goal is to design and implement a simplified webcrawler. The system should accept an initial webpage to crawl, such as:

```
https://en.wikipedia.org/wiki/Earth
```

from which it should progressively discover all linked pages. To limit the amount of work performed by the crawler, it should accept a maximum number of distinct pages to visit, for example, `1000`.

As the crawler visits pages, it should build a general representation of how pages link to each other. Upon completion, it should print the complete list of pages visited, sorted by decreasing *in-degree* (ie, how many pages link to it). For example:

```
https://en.wikipedia.org/wiki/Sun   18
https://en.wikipedia.org/wiki/Ion   12
...
```

### Tasks
{: .no_toc }

<script type="text/javascript" src="{{ "/assets/js/toggle-answer.js" | absolute_url }}"></script>
<a class="toggle-all-answers-button">Show all answers ▽</a>

1. <div class="question">Implement the webcrawler described above. Use the programming language and tools of your choice. 
    <span class="toggle-answer-icon">▽</span>
    <div class="answer">Answer: This is the answer this is the answer this is the answer.</div>
    </div>

2. <div class="question">Document any important design decisions and assumptions you made along the way, and their associated tradeoffs.
    <span class="toggle-answer-icon">▽</span>
    <div class="answer">Answer: This is the answer this is the answer this is the answer.</div>
    </div>


### Duration
{: .no_toc }

Spend a maximum of 2 hours.


### Evaluation criteria
{: .no_toc }

Your submission will be evaluated by an engineer according to the following criteria:

* Criterion 1
* Criterion 2
* Criterion 3


---


## Grading rubric
{: .d-inline-block } 
For reviewer
{: .label .label-yellow }


--- 


[Notify me when Interview Pro launches](/notify-me){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
[Give feedback](/give-feedback){: .btn .fs-5 .mb-4 .mb-md-0 }


© 2020 Interview Pro
{: .fs-1 .fw-300 .text-grey-dk-000}

