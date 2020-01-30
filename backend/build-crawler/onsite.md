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

1. Describe the sequence of operations the crawler needs to perform, to produce the desired output.

2. Write a possible block diagram for the webcrawler.

3. How can the crawler enforce that the maximum number of distinct pages to visit is, say, `1000`?

4. What data structure should the crawler use to represent how pages link to each other?
    1. Where can the crawler store this data structure?
    2. What are the tradeoffs between storing this data structure *in memory* vs. *in disk*?
    3. How would you store this data struture in a *relational database*, such as MySQL?
    4. How would you store this data struture in a *key-value database*, such as Redis?

5. What metric can we use to benchmark the *speed* of different crawlers?
    1. What factors (internal or external) influence this metric?
    2. What design changes could we make to improve the performance of the crawler we previously designed?

6. Is the crawler we previously designed capable of fetching multiple webpages in parallel?
    1. How would you extend the design to allow parallel fetching?
    2. How would you implement parallel fetching using *multiple processes*?
    3. How would you implement parallel fetching using a *single process*?
    4. How would you implement parallel fetching using a *single thread*?

7. What types of errors can the crawler encounter while navigating webpages?
    1. How can we handle 4xx errors?
    2. How can we handle 5xx errors?
    3. How can we handle DNS errors?

8. How would the crawler handle query parameters in a URL?


---


## Grading rubric
{: .d-inline-block } 
After onsite
{: .label .label-yellow }


### Example solution
{: .no_toc }

here


--- 


[Notify me when Interview Pro launches](https://notify-form){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
[Give feedback](https://feedback-form){: .btn .fs-5 .mb-4 .mb-md-0 }

