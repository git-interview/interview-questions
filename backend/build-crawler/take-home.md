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
        <td>
            The solution accepts an initial webpage to crawl, for example, <code>https://apple.com</code>.
        </td>
        <td class="grade-col">
            <input type="radio" name="fr1" id="fr1-no"><label for="fr1-no">&nbsp;No</label>
            &nbsp;&nbsp;&nbsp;
            <input type="radio" name="fr1" id="fr1-yes"><label for="fr1-yes">&nbsp;Yes</label>
        </td>
    </tr>
    <tr>
        <td>
            The solution strictly respects the limit of pages to visit, for example, <code>10</code>.
        </td>
        <td class="grade-col">
            <input type="radio" name="fr2" id="fr2-no"><label for="fr2-no">&nbsp;No</label>
            &nbsp;&nbsp;&nbsp;
            <input type="radio" name="fr2" id="fr2-yes"><label for="fr2-yes">&nbsp;Yes</label>
        </td>
    </tr>
    <tr>
        <td>
            The solution correctly prints pages sorted by decreasing in-degree.
        </td>
        <td class="grade-col">
            <input type="radio" name="fr3" id="fr3-no"><label for="fr3-no">&nbsp;No</label>
            &nbsp;&nbsp;&nbsp;
            <input type="radio" name="fr3" id="fr3-yes"><label for="fr3-yes">&nbsp;Yes</label>
        </td>
    </tr>
</table>


<strong>Code architecture</strong>
<table>
    <tr>
        <td>
            The code is composed of building blocks that are defined in a understandable, coherent, and elegant manner. For example, the solution may consist of classes to represent domain objects, such as <code>Crawler</code>, <code>Page</code> or <code>Link</code>.
        </td>
        <td class="grade-col">
            <input type="radio" name="ca1" id="ca1-no"><label for="ca1-no">&nbsp;No</label>
            &nbsp;&nbsp;&nbsp;
            <input type="radio" name="ca1" id="ca1-yes"><label for="ca1-yes">&nbsp;Yes</label>
        </td>
    </tr>
    <tr>
        <td>
            The building blocks hide the implementation details. For example, we can change the persistence method of the graph of webpages (memory or in disk) without changing all codebase. 
        </td>
        <td class="grade-col">
            <input type="radio" name="ca2" id="ca2-no"><label for="ca2-no">&nbsp;No</label>
            &nbsp;&nbsp;&nbsp;
            <input type="radio" name="ca2" id="ca2-yes"><label for="ca2-yes">&nbsp;Yes</label>
        </td>
    </tr>
    <tr>
        <td>
            The building blocks are reusable, and can be easily extended with new functionality. For example, 
        </td>
        <td class="grade-col">
            <input type="radio" name="ca3" id="ca3-no"><label for="ca3-no">&nbsp;No</label>
            &nbsp;&nbsp;&nbsp;
            <input type="radio" name="ca3" id="ca3-yes"><label for="ca3-yes">&nbsp;Yes</label>
        </td>
    </tr>
    <tr>
        <td>
            The interface of each building block is simple, clean, and natural.
        </td>
        <td class="grade-col">
            <input type="radio" name="ca4" id="ca4-no"><label for="ca4-no">&nbsp;No</label>
            &nbsp;&nbsp;&nbsp;
            <input type="radio" name="ca4" id="ca4-yes"><label for="ca4-yes">&nbsp;Yes</label>
        </td>
    </tr>
</table>


<strong>Criteria</strong>
<table>
    <tr>
        <td>
            c1
        </td>
        <td class="grade-col">
            <input type="radio" name="c1" id="c1-no"><label for="c1-no">&nbsp;No</label>
            &nbsp;&nbsp;&nbsp;
            <input type="radio" name="c1" id="c1-yes"><label for="c1-yes">&nbsp;Yes</label>
        </td>
    </tr>
    <tr>
        <td>
            c2
        </td>
        <td class="grade-col">
            <input type="radio" name="c2" id="c2-no"><label for="c2-no">&nbsp;No</label>
            &nbsp;&nbsp;&nbsp;
            <input type="radio" name="c2" id="c2-yes"><label for="c2-yes">&nbsp;Yes</label>
        </td>
    </tr>
    <tr>
        <td>
            c3
        </td>
        <td class="grade-col">
            <input type="radio" name="c3" id="c3-no"><label for="c3-no">&nbsp;No</label>
            &nbsp;&nbsp;&nbsp;
            <input type="radio" name="c3" id="c3-yes"><label for="c3-yes">&nbsp;Yes</label>
        </td>
    </tr>
    <tr>
        <td>
            c4
        </td>
        <td class="grade-col">
            <input type="radio" name="c4" id="c4-no"><label for="c4-no">&nbsp;No</label>
            &nbsp;&nbsp;&nbsp;
            <input type="radio" name="c4" id="c4-yes"><label for="c4-yes">&nbsp;Yes</label>
        </td>
    </tr>
</table>


--- 


[Notify me when Interview Pro launches](/notify-me){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
[Give feedback](/give-feedback){: .btn .fs-5 .mb-4 .mb-md-0 }


© 2020 Interview Pro
{: .fs-1 .fw-300 .text-grey-dk-000}

