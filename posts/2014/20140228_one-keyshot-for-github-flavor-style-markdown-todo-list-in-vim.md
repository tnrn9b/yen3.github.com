<!--
.. link: 
.. description: 
.. tags: all
.. date: 2014/02/28 17:14:13
.. title: Two keyshots for github-flavor style markdown todo list in vim
.. slug: 20140228_one-keyshot-for-github-flavor-style-markdown-todo-list-in-vim
-->

原本想要寫一個 plugin，但是我對 vim script 不太熟加上其實自己並不是這麼清楚想要什麼功能，等過一陣子真的需要的時候再自己寫的東西收集後再說。

以 github-flavored markdown 來說，裡面有一個 check 的功能，只要在你的 markdown 裡面寫

```
* [ ] To do list item
* [ ] To do list item 2
```
github 會把 `[ ] `轉換成 html checkbox，寫是簡單，只是有時候要標記完成實在是很麻煩 (很多項的時候)，所以自己土炮了一個簡單的 vim 快捷鍵。在 `$HOME/.vimrc` 貼上

```
function! CheckMarkdownTodoItem()
    let s = getline(line('.')) 
    if match(s, '\[x\]') > -1
        s/\[x\]/\[ \]/ 
        s/ (Finished: \(.* .*\))//
    elseif match(s, '\[ \]') > -1
        s/\[ \]/\[x\]/ 

        call cursor(line('.'), $)
        exe "normal! A (Finished: " . strftime("%a %Y-%m-%d") . " " . strftime("%T") .")\<Esc>"
    else
        echo "No Item"
    endif
endfunction

function! AddNewMarkdownToDo()
    exe "normal! o* [ ]  \<Esc>"
endfunction

autocmd FileType mkd,markdown nmap <leader>gc :call AddNewMarkdownToDo()<cr>
autocmd FileType markdown nmap <C-d>  :call CheckMarkdownTodoItem()<cr>
```

在 markdown filetype ，對這樣子的 item

```
* [ ] To do list item
* [ ] To do list item 2
```

按 Ctrl + D 之後即可變成

```
* [x] To do list item (Finished: Fri 2014-02-28 17:21:14)
* [x] To do list item 2 (Finished: Fri 2014-02-28 17:21:15)
```

再按一次  Ctrl + D 就變成

```
* [ ] To do list item
* [ ] To do list item 2
```

是一個方便的小功能，到目前為止是這個功能最重要，以後想到再慢慢加。

而在空白行中按 `\gc` 的話，則會新增一個 todo item  如下

```
* [ ] 
```

就可以輸入你想要新增的待辦事項了。
