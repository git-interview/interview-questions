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
    <dd>3 hours</dd>

    <dt>Difficulty</dt>
    <dd>Medium</dd>

    <dt>Topics</dt>
    <dd>Distributed Systems</dd>

    <dt>Format</dt>
    <dd>Take-home</dd>
</dl>


---


#### On this page
{: .no_toc }

1. TOC
{: toc}


---


## Problem statement
{: .d-inline-block } 
For candidate 
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

### Tasks
{: .no_toc }

1. Implement the webcrawler described above. Use the programming language and tools of your choice. 

2. Include any additional information that you think will help the reviewer understand your solution. For example: important design decisions, assumptions, or future improvements.


### Duration
{: .no_toc }

Spend a maximum of 3 hours.


### Grading criteria
{: .no_toc }

Your submission will be graded by an engineer according to the following criteria:

* Code quality
* Design decisions


---


## Solution
{: .d-inline-block } 
For reviewer
{: .label .label-yellow }

<script type="text/javascript" src="{{ "/assets/js/toggle-solution.js" | absolute_url }}"></script>


<a href="https://gist.github.com/git-interview/36afa27c5c1b8476308ad5a9de79dff9/archive/master.zip">Download ZIP</a>
&nbsp;&nbsp;|&nbsp;&nbsp;
<a class="toggle-solution-button">Show solution ▽</a>

<div class="solution">
    <script src="https://gist.github.com/git-interview/36afa27c5c1b8476308ad5a9de79dff9.js?file=readme.md"></script>
    <script src="https://gist.github.com/git-interview/36afa27c5c1b8476308ad5a9de79dff9.js?file=solution.py"></script>
    <script src="https://gist.github.com/git-interview/36afa27c5c1b8476308ad5a9de79dff9.js?file=output.log"></script>
    <script src="https://gist.github.com/git-interview/36afa27c5c1b8476308ad5a9de79dff9.js?file=Dockerfile"></script>
    <script src="https://gist.github.com/git-interview/36afa27c5c1b8476308ad5a9de79dff9.js?file=requirements.txt"></script>
</div>


---


## Grading rubric
{: .d-inline-block } 
For reviewer
{: .label .label-yellow }


<strong>Functional requirements</strong>
<table>
    <tr>
        <td><strong>Initial page.</strong> We can specify an initial webpage to crawl, for example, <code>https://apple.com</code>.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Max pages.</strong> We can specify the maximum number of pages to crawl, eg, <code>10</code>. This limit is strictly respected.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>In-degrees.</strong> The solution correctly prints pages sorted by decreasing in-degree.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
</table>


<strong>Code architecture</strong>
<table>
    <tr>
        <td><strong>Usable.</strong> The crawler API is easy to understand and use. It's possible to invoke the crawler without knowing its implementation details.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Modular.</strong> The code is divided into small building blocks that are easier to understand, instead of one large block. For example, it uses classes to represent domain objects, such as <code>Crawler</code>, <code>Page</code> or <code>Link</code>.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Understandable.</strong> The purpose of each building block (eg, class or function) is easy to understand. The input and output parameters are natural and appropriate.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Extensible.</strong> It's easy to add new functionality. For example, extending the crawler to parse PDF documents, in addition to HTML documents.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
</table>


<strong>Code readability</strong>
<table>
    <tr>
        <td><strong>Clear naming.</strong> The solution uses clear, self-explanatory names for variables. It's easy to understand the purpose of each function from its name only.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Useful documentation.</strong> Each class or function includes a description of its purpose, and how it should be used by another developer. It omits implementation details.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Useful comments.</strong> Comments describe <em>why</em>, instead of <em>how</em>. It helps the reader understand underlying design decisions, instead of just re-stating the code.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Consistent style.</strong> The code adopts a style that is consistent throughout. For example, indentation and casing are the same in all codebase.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
</table>


<strong>Concurrency</strong>
<table>
    <tr>
        <td><strong>Capable.</strong> The solution is able to fetch multiple pages concurrently. For example, it uses multiple processes, threads, or coroutines.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Adjustable.</strong>The user of the crawler can easily adjust the level of concurrency, for example, the number of workers used.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Race-free.</strong> The implementation avoids race conditions and deadlocks. For example, when using concurrent workers, the correct mechanisms are used to ensure that each page is only processed once, and the maximum number of pages is respected.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
</table>


<strong>Robustness</strong>
<table>
    <tr>
        <td><strong>Handles rate limits.</strong> The solution appropriately handles rate-limiting by the server. For example, it fetches pages within each domain by issuing a maximum number of requests per second.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Handles GET errors.</strong> The solution appropriately handles the various types of errors that can occur while fetching a webpage. For example, it distinguishes between DNS resolution errors, timeouts, 5xx status, and 4xx status, and determines which of these are retryable at a later time.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
</table>




<strong>Extras</strong>
<table>
    <tr>
        <td><strong>Automated tests.</strong> The solution implements unit or functional tests.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Reproducible environment.</strong> The solution includes automated scripts to build the solution and provision all necessary dependencies. For example, it includes a Dockerfile.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
</table>


<strong>Generality</strong>
<table>
    <tr>
        <td>Content types beyond HTML</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
</table>


<strong>Assumptions and limitations</strong>
<table>
    <tr>
        <td><strong>Assumptions</strong>. The candidate adequately documented the assumptions made. For example, whether duplicate links between pages are counted.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
    <tr>
        <td><strong>Limitations</strong>. The candidate clearly identified limitations in the code, and dimensions for future improvement. For example, improved architecture, readability, concurrency, or robustness.</td>
        <td class="grade-col">
            <select>
                <option value="pick-one" selected disabled hidden>Choose</option>
                <option value="excellent">Excellent</option>
                <option value="good">Good</option>
                <option value="poor">Poor</option>
                <option value="very-poor">Very poor</option>
            </select>
        </td>
    </tr>
</table>


--- 


[Notify me when Interview Pro launches](/notify-me){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
[Give feedback](/give-feedback){: .btn .fs-5 .mb-4 .mb-md-0 }


© 2020 Interview Pro
{: .fs-1 .fw-300 .text-grey-dk-000}

