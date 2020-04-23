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

Spend a maximum of 2 hours.


### Evaluation criteria
{: .no_toc }

Your submission will be evaluated by an engineer according to the following criteria:

* Criterion 1
* Criterion 2
* Criterion 3


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
        <th>Dimension</th>
        <th>Score</th>
        <th>Weight</th>
    </tr>
    <tr>
        <td>Functionality</td>
        <td>
            <br>
            <input type="radio" id="male" name="gender" value="male">
            <label for="male"><strong>3 points</strong>: Perfect functionality. Search function works. Clicking on a still thumbnail launches a lightbox view with navigation. Able to navigate between animated GIFs in the lightbox modal.</label>
            <br><br>
            <input type="radio" id="female" name="gender" value="female">
            <label for="female"><strong>2 points</strong>: Issues or missing features hinder user experience. For example, navigation may be missing from the lightbox.</label>
            <br><br>
            <input type="radio" id="other" name="gender" value="other">
            <label for="other"><strong>1 point</strong>: Unable to interact with the GIF browsing app; page is completely broken.</label>
            <br>
            <br>
        </td>
        <td>1</td>
    </tr>
    <tr>
        <td>Functionality</td>
        <td>
            <br>
            <input type="radio" id="male2" name="gender2" value="male2">
            <label for="male2"><strong>3 points</strong>: Perfect functionality. Search function works. Clicking on a still thumbnail launches a lightbox view with navigation. Able to navigate between animated GIFs in the lightbox modal.</label>
            <br><br>
            <input type="radio" id="female2" name="gender2" value="female2">
            <label for="female2"><strong>2 points</strong>: Issues or missing features hinder user experience. For example, navigation may be missing from the lightbox.</label>
            <br><br>
            <input type="radio" id="other2" name="gender2" value="other2">
            <label for="other2"><strong>1 point</strong>: Unable to interact with the GIF browsing app; page is completely broken.</label>
            <br>
            <br>
        </td>
        <td>1</td>
    </tr>
</table>



Format
    Dimension           1 = below/no     2 = avg/maybe    3 = above/yes
    Dimension           1                2                3
    Dimension           1                2                3
    Dimension           1                2                3
    Dimension           1                2                3
    Dimension           1                2                3
    Dimension           1                2                3
    Dimension           1                2                3
    Dimension           1                2                3
    -----------------------------------------------------------
    Overall weighed score            0 - 10




Dimensions
    Code quality (same criteria as a code review)
        Readability
        Comments
        Reusability
        Reproducible environment
        Does it meet the spec
            Does it accept a starting URL?
            Does it respect max_pages?
            Does it print in-degrees?
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

