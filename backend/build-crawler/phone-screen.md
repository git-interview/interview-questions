---
grand_parent: "Backend"
parent: "Build a web crawler"
title: "Phone screen"
nav_order: 1
layout: default
permalink: "/backend-questions/build-a-web-crawler/phone-screen"
---


# Phone screen
{: .no_toc }

<dl>
    <dt>Task</dt>
    <dd>Design and implement a simple web crawler.</dd>

    <dt>Duration</dt>
    <dd>30 mins</dd>

    <dt>Difficulty</dt>
    <dd>Adaptive</dd>

    <dt>Topics</dt>
    <dd>Distributed Systems</dd>

    <dt>Format</dt>
    <dd>Phone Screen</dd>
</dl>


--- 


1. TOC
{: toc}


---


## Coding

Requires coderpad.
Write from scratch, in any language.


## Discussion

Scenario: crawler of webpages

1. Describe the sequence of operations the crawler needs to perform, to produce the desired output.

2. How would you architect the crawler? What's the responsibility of each component?

3. How can the crawler enforce that the maximum number of distinct pages to visit is, say, `1000`?

4. What data structure should the crawler use to represent how pages link to each other?

5. What metric can we use to benchmark the *speed* of different crawlers?

6. Is the crawler we previously designed capable of fetching multiple webpages in parallel?

7. What types of errors can the crawler encounter while navigating webpages?

8. How would the crawler handle query parameters in a URL?










































## Scenario
{: .d-inline-block } 
During phone screen
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

---


## Questions

1. Implement the webcrawler described above, using a programming language of your choice. 

2. Document any important assumptions or decisions you made along the way, and their associated tradeoffs.


---


## Grading rubric
{: .d-inline-block } 
After phone screen
{: .label .label-yellow }


### Example solution
{: .no_toc }

here


--- 


[Notify me when Interview Pro launches](https://notify-form){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
[Give feedback](https://feedback-form){: .btn .fs-5 .mb-4 .mb-md-0 }

