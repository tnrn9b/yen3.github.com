<!--
.. link: 
.. description: 
.. tags: all
.. date: 2013/11/14 22:20:10
.. title: ctags add a user-defined language
.. slug: 20131114_ctags-add-a-user-defined-language
-->

最近在工作上需要，但是在公司裡面試不出來，所以索性回來再試。

ctags 讀 assembly 時，有些 label 並不是長成這個樣子 `^.*:` (用 regular expression)。以我遇到的範例是會長成像這樣子

```asm
.label test:
    add r1, r2, r3
``` 
        
其實 test 也是 tag，但是預設不會加到 tag list。參考 [document](http://ctags.sourceforge.net/EXTENDING.html) 所提的方法。在 `~/.ctags` 裡加上。

    --langdef=asm
    --langmap=asm:.s
    --regex-md32asm=/^(.*):/\1/d,defintion/
    --regex-md32asm=/.label (.*)/\1/d,defintion/
    
就可以很順利的處理這種 label 了，再配合 [cscope_maps.vim](http://cscope.sourceforge.net/cscope_maps.vim) 就可以很開心的在 vim 裡跳來跳去了~

其實要讓 tagbar 對 markdown 檔案產生相對應的 tag 也是用這個方法，同樣在 `~/.ctags` 裡面加上

```
--langdef=markdown
--langmap=markdown:.mkd
--regex-markdown=/^#[ \t]+(.*)/\1/h,Heading_L1/
--regex-markdown=/^##[ \t]+(.*)/\1/i,Heading_L2/
--regex-markdown=/^###[ \t]+(.*)/\1/k,Heading_L3/
```
就可以了。

做個簡單筆記，希望以後自己可以持續改善自己的工具。