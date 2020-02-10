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
    <dd>Design a web crawler and discuss tradeoffs.</dd>

    <dt>Duration</dt>
    <dd>45 mins</dd>

    <dt>Difficulty</dt>
    <dd>Adaptive</dd>

    <dt>Topics</dt>
    <dd>Distributed Systems</dd>

    <dt>Format</dt>
    <dd>Onsite</dd>
</dl>


--- 


1. TOC
{: toc}


---


## Scenario
{: .d-inline-block }
During onsite
{: .label .label-green }

Our goal is to design a simplified webcrawler. The system should accept an initial webpage to crawl, such as:

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


---


## Questions
{: .d-inline-block } 
During onsite
{: .label .label-green }


<script type="text/javascript" src="{{ "/assets/js/toggle-answer.js" | absolute_url }}"></script>
<span class="toggle-all-answers">Show all answers ▷</span>


1. <div class="question">Describe the sequence of operations the crawler needs to perform, to produce the desired output. 
    <div class="answer">
    Answer: This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this.
        <img src="/backend/build-crawler/cover.png" width="100" />
        <br />
    Now, is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</div></div>

2. <span class="question">Write a possible block diagram for the webcrawler. <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>

3. <span class="question">How can the crawler enforce that the maximum number of distinct pages to visit is, say, `1000`? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>

4. <span class="question">What data structure should the crawler use to represent how pages link to each other? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    1. <span class="question">Where can the crawler store this data structure? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    2. <span class="question">What are the tradeoffs between storing this data structure *in memory* vs. <span class="question">*in disk*? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    3. <span class="question">How would you store this data struture in a *relational database*, such as MySQL? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    4. <span class="question">How would you store this data struture in a *key-value database*, such as Redis? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>

5. <span class="question">What metric can we use to benchmark the *speed* of different crawlers? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    1. <span class="question">What factors (internal or external) influence this metric? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    2. <span class="question">What design changes could we make to improve the performance of the crawler we previously designed? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>

6. <span class="question">Is the crawler we previously designed capable of fetching multiple webpages in parallel? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    1. <span class="question">How would you extend the design to allow parallel fetching? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    2. <span class="question">How would you implement parallel fetching using *multiple processes*? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    3. <span class="question">How would you implement parallel fetching using a *single process*? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    4. <span class="question">How would you implement parallel fetching using a *single thread*? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>

7. <span class="question">What types of errors can the crawler encounter while navigating webpages? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    1. <span class="question">How can we handle 4xx errors? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    2. <span class="question">How can we handle 5xx errors? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>
    3. <span class="question">How can we handle DNS errors? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>

8. <span class="question">How would the crawler handle query parameters in a URL? <span class="answer">This is the answer to the question this is the answer to the question this is the qnswer this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this this is the answer this.</span> </span>






1. <span class="question">Question 1
    <span class="answer">Answer 1</span>
</span>


2. <span class="question">Question 2
    <span class="answer">Answer 2</span>
</span>


---


## Grading rubric
{: .d-inline-block } 
After onsite
{: .label .label-yellow }


### Example solution
{: .no_toc }

here


--- 


[Notify me when Interview Pro launches](/notify-me){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
[Give feedback](/give-feedback){: .btn .fs-5 .mb-4 .mb-md-0 }


© 2020 Interview Pro
{: .fs-1 .fw-300 .text-grey-dk-000}

