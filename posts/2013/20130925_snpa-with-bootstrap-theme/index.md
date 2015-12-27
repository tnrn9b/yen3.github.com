<!--
.. link: 
.. description: 
.. tags: all, tweet, snpa
.. date: 2013/09/25 22:03:02
.. title: SNPA: bootstrap theme
.. slug: 20130925_snpa-with-bootstrap-theme
-->

## New Function

* typesetting with [bootstrap 2.3.2](http://getbootstrap.com/2.3.2/)


## Murmur

老實說一直知道 bootstrap，但是一直不知道怎麼用(也沒啥機會用 XD)，索性就不用 XD。(註: 後來才發現原來出到 3.0 了 XD)

但是這件事一直到我自己寫了 Simple Nikola Post Admin 之後好像不行，看一看自己一開始的 html (參考這篇 [About simple nikola post admin | Lambda Mind 2](http://yen3.github.io/posts/20130922_about-simple-nikola-post-admin.html))，似乎真的有點讓人傷心 XD。

所以今天晚上利用很想睡的時機，把 bootstrap 套用，另外 flask 指定使用 jinja2 (Django 用的也是同一套)。利用 template hierarchy 的概念，再加上 [python-livereload](https://github.com/lepture/python-livereload) 靠 browser 不斷的自己重新刷畫面 XD，很快就做出來，雖然沒什麼原創性 (對不起，我美術不好 XD)，不過至少一般使用是 ok 的。畫面如下: 

* 主畫面

<a href="http://www.flickr.com/photos/24606632@N05/9933744814/" title="Flickr 上 yen3rc 的 Screen Shot 2013-09-25 at 10.01.53 PM"><img src="https://farm6.staticflickr.com/5505/9933744814_a73f056968.jpg" width="500" height="411" alt="Screen Shot 2013-09-25 at 10.01.53 PM"></a>

* 編輯文章

<a href="http://www.flickr.com/photos/24606632@N05/9933721636/" title="Flickr 上 yen3rc 的 Screen Shot 2013-09-25 at 10.01.51 PM"><img src="https://farm8.staticflickr.com/7295/9933721636_68a8fceebd.jpg" width="500" height="411" alt="Screen Shot 2013-09-25 at 10.01.51 PM"></a>

* 儲存文章

<a href="http://www.flickr.com/photos/24606632@N05/9933703605/" title="Flickr 上 yen3rc 的 Screen Shot 2013-09-25 at 10.02.28 PM"><img src="https://farm8.staticflickr.com/7384/9933703605_a09f482431.jpg" width="500" height="411" alt="Screen Shot 2013-09-25 at 10.02.28 PM"></a>

* 發佈

<a href="http://www.flickr.com/photos/24606632@N05/9933721816/" title="Flickr 上 yen3rc 的 Screen Shot 2013-09-25 at 10.02.44 PM"><img src="https://farm6.staticflickr.com/5339/9933721816_ecdd43b9af.jpg" width="500" height="411" alt="Screen Shot 2013-09-25 at 10.02.44 PM"></a>

大概再把一個 bug 修一修就可以發佈 v0.1 了，到底要不要利用這個機會趁機學學怎麼包 python package 勒 XD。