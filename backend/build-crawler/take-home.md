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


<table>
    <tr>
        <th>Criterion</th>
        <th>Grade</th>
    </tr>
    <tr>
        <td>Functionality</td>
        <td>
            <br>
            <input type="radio" name="criterion" id="excellent">
            <label for="excellent">
                <strong>Excellent</strong>: The solution runs and meets all requirements: it accepts an initial webpage to crawl, strictly respects the limit of pages to visit, and correctly prints pages sorted by decreasing in-degree. The solution also handles implicit corner cases well, such as when the initial page contains no links, or the initial page is unfetchable.
            </label>
            <br><br>
            <input type="radio" name="criterion" id="good">
            <label for="good">
                <strong>Good</strong>: The solution runs and meets most requirements. It might handle a requirement imperfectly, such as crawling more pages than the specified limit. It might miss some corner cases, such as when the initial page is unfetchable or has no links.
            </label>
            <br><br>
            <input type="radio" name="criterion" id="poor">
            <label for="poor">
                <strong>Poor</strong>: The solution runs, but fails to meet most of the requirements.
            </label>
            <br><br>
            <input type="radio" name="criterion" id="very-poor">
            <label for="very-poor">
                <strong>Very poor</strong>: The solution doesn't run, or fails to meet any requirement.
            </label>
            <br><br>
        </td>
    </tr>
    <tr>
        <td>Criterion</td>
        <td>
            <br>
            <input type="radio" name="criterion" id="excellent">
            <label for="excellent">
                <strong>Excellent</strong>: Details
            </label>
            <br><br>
            <input type="radio" name="criterion" id="good">
            <label for="good">
                <strong>Good</strong>: Details
            </label>
            <br><br>
            <input type="radio" name="criterion" id="poor">
            <label for="poor">
                <strong>Poor</strong>: Details
            </label>
            <br><br>
            <input type="radio" name="criterion" id="very-poor">
            <label for="very-poor">
                <strong>Very poor</strong>: Details
            </label>
            <br><br>
        </td>
    </tr>
    <tr>
        <td>Criterion</td>
        <td>
            <br>
            <input type="radio" name="criterion" id="excellent">
            <label for="excellent">
                <strong>Excellent</strong>: Details
            </label>
            <br><br>
            <input type="radio" name="criterion" id="good">
            <label for="good">
                <strong>Good</strong>: Details
            </label>
            <br><br>
            <input type="radio" name="criterion" id="poor">
            <label for="poor">
                <strong>Poor</strong>: Details
            </label>
            <br><br>
            <input type="radio" name="criterion" id="very-poor">
            <label for="very-poor">
                <strong>Very poor</strong>: Details
            </label>
            <br><br>
        </td>
    </tr>
    <tr>
        <td>Criterion</td>
        <td>
            <br>
            <input type="radio" name="criterion" id="excellent">
            <label for="excellent">
                <strong>Excellent</strong>: Details
            </label>
            <br><br>
            <input type="radio" name="criterion" id="good">
            <label for="good">
                <strong>Good</strong>: Details
            </label>
            <br><br>
            <input type="radio" name="criterion" id="poor">
            <label for="poor">
                <strong>Poor</strong>: Details
            </label>
            <br><br>
            <input type="radio" name="criterion" id="very-poor">
            <label for="very-poor">
                <strong>Very poor</strong>: Details
            </label>
            <br><br>
        </td>
    </tr>
</table>



Observables
    Code / build scripts / tests
    Writeup

Dimensions
    Meeting requirements, functionality
    Design: classes, interfaces, simple, reusable
    Concurrency
    Error handling
    Testing
    Readability, comments, documentation, naming, style, consistency
    Clarity of writeup
    Understanding of limitations mentioned
    Environment / build scripts


    Code quality (same criteria as a code review)
        Readability, Comments
        Reusability
        Reproducible environment
        Extra features
            Concurrency
            Rate limiting
            Content types
            Page retries
            Exception handling
            Tests
    Understanding of design decisions, limitations, improvements
        Clarity of communication


--- 


[Notify me when Interview Pro launches](/notify-me){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
[Give feedback](/give-feedback){: .btn .fs-5 .mb-4 .mb-md-0 }


© 2020 Interview Pro
{: .fs-1 .fw-300 .text-grey-dk-000}

