<!--
.. link: 
.. description: 
.. tags: all, software
.. date: 2013/09/15 23:29:53
.. title: Push without username/passwd in Github
.. slug: 20130915_push-without-username-passwd-in-github
-->

這方法不是我發明的，但是找到就備忘一下。

方法來自 [authentication - Git push requires username and password - Stack 
Overflow](http://stackoverflow.com/questions/6565357/git-push-requires-username-and-password) 
照著這篇文章的說明，只要把自己的 repo 改成 ssh 就行

```bash
git remote set-url origin git@github.com:username/repo.git
```

所以完之後，在 nikola 的 output 的 github repo 上我輸入

```bash
git push -u origin master
```

就可以上傳了。所以現在就可以寫簡單的 Makefile 來做一些事了。

```Makefile
all:
        nikola build && nikola auto
deploy:
        cd output && git add posts/* && git commit -a -m "automatic push" && 
        git push -u origin master
```

不過其實要做什麼事我其實還沒有很清楚，想到再加上來好了。