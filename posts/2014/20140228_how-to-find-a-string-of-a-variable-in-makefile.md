<!--
.. link: 
.. description: 
.. tags: all, note, murmur
.. date: 2014/02/28 17:07:43
.. title: How to find a string of a variable in Makefile ?
.. slug: 20140228_how-to-find-a-string-of-a-variable-in-makefile
-->

其實這不是一個很難的問題，只是我對 makefile 格式不熟，解決這個問題大部分的時間是在找文件。
為什麼會有這個問題，只是上班的時候遇到解決了就記下來了 XD。

以下面的例子來說，要在 `$(OPTION)` 裡找是否有 `__TEST_2__` 這個字串:
```
OPTION = __TEST_1__
OPTION += __TEST_2__
ifneq (, $(findstring "__TEST_2__", $(OPTION)))
    RESULT = "find"
else
    RESULT = "Not find"
endif

all:
	@echo $(RESULT)
	@echo $(OPTION)
```

做個簡單的筆記。


## Reference

這邊的 reference 是我找的時候所看到的資料，再加上 stackoverflow 的解說，對 makefile 有興趣的人可以看看 XD。

* [跟我一起写 Makefile（一） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2886)
* [跟我一起写 Makefile（二） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2887)
* [跟我一起写 Makefile（三） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2888)
* [跟我一起写 Makefile（四） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2889)
* [跟我一起写 Makefile（五） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2890)
* [跟我一起写 Makefile（六） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2891)
* [跟我一起写 Makefile（七） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2892)
* [跟我一起写 Makefile（八） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2893)
* [跟我一起写 Makefile（九） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2894)
* [跟我一起写 Makefile（十） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2895)
* [跟我一起写 Makefile（十一） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2896)
* [跟我一起写 Makefile（十二） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2898)
* [跟我一起写 Makefile（十三） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2898)
* [跟我一起写 Makefile（十四） - 陈皓专栏　【空谷幽兰，心如皓月】 - 博客频道 - CSDN.NET](http://blog.csdn.net/haoel/article/details/2899)