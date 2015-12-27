<!--
.. link: 
.. description: 
.. tags: all, programming
.. date: 2013/09/14 21:05:40
.. title: Fix error about generating pandoc-style html in nikola
.. slug: nikola pandoc_compile_error_20130914
-->
先聲明，這不是很大的錯誤，這篇文章僅僅記錄我找到錯誤的原因。在 nikola 裡面可以使用 pandoc 來生出 html 文件，我看了很開心，改了 `conf.py` 之後執行發現 ...

```bash
> nikola build
Scanning posts..done!
.  render_posts:cache/posts/20130914_why_nikola.html
########################################
TaskError - taskid:render_posts:cache/posts/20130914_why_nikola.html
PythonAction Error
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/site-packages/doit/action.py", line 324, in execute
    returned_value = self.py_callable(*self.args, **kwargs)
  File "/usr/local/lib/python2.7/site-packages/nikola/plugins/compile/pandoc.py", line 59, in compile_html
    subprocess.check_call((pandoc_path, '-o', dest, source))
  File "/usr/local/Cellar/python/2.7.5/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 537, in check_call
    retcode = call(*popenargs, **kwargs)
  File "/usr/local/Cellar/python/2.7.5/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 524, in call
    return Popen(*popenargs, **kwargs).wait()
  File "/usr/local/Cellar/python/2.7.5/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 711, in __init__
    errread, errwrite)
  File "/usr/local/Cellar/python/2.7.5/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 1308, in _execute_child
    raise child_exception
OSError: [Errno 2] No such file or directory
```

這其實是一個很白爛的問題，但是其實看到出錯訊息就知道為什麼了 … 我原本以為是找不到 pandoc 位在那，後來發現他是用 `which` 去找，理論上應該是找的到才對，後來發現，事情不是我想的這麼簡單，我查了一下出錯的地方 `/usr/local/lib/python2.7/site-packages/nikola/plugins/compile/pandoc.py", line 59`，那一行是這樣子寫的:

```Python
subprocess.check_call((pandoc_path, '-o', source, dest))
```

其實這一行的 source 和 dest 參數放反了，反過來就解決了，所以我就改成:

```Python
subprocess.check_call((pandoc_path, '-o', dest, source))
```

但是還是出錯 … Orz，後來我把每個變數印出來發現其中的 `pandoc_path` 長成:

```
'/Users/yen3/.cabal/bin/pandoc\n'
```

兇手找到了 (但是其實我蠻想知道 `which` 找到的東西為什麼會多一個 `\n`)，所以最後那一行改成:

```Python
subprocess.check_call((pandoc_path.split('\n')[0], '-o', dest, source))
```

就能編譯成功了，如此一來就又有一個 blog system 可以寫 pandoc-style markdown 了。

我是還蠻想送 patch 給原作者啦，剛剛我有送一個 issue 
上去，希望我不要被認為是白目啊 XDXD。 

* * *

後記: 送了一個 [issue](https://github.com/getnikola/nikola/issues/709) 
給原作者後，他不到十分鐘就修復了還抱歉 … 好 nice 的外國人喔~!
