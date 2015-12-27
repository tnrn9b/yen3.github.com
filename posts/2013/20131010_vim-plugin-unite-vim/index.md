<!--
.. link: 
.. description: 
.. tags: all, software, note
.. date: 2013/10/10 22:23:44
.. title: Vim plugin: Unite.vim
.. slug: 20131010_vim-plugin-unite-vim
-->

關於 [Shougo/unite.vim](https://github.com/Shougo/unite.vim) 沒什麼好說的，是一個用了會上癮的 plugin，用了它之後，ctrl+p 和 command-T 都可以不用了，開心 XD。

在此稍微貼上自己關於這方面的 vim 設定檔

* 安裝 plugin 部分 (這邊使用 [Shougo/neobundle.vim](https://github.com/Shougo/neobundle.vim))

```vim
NeoBundle 'Shougo/unite.vim'
NeoBundle 'tsukkee/unite-tag'
NeoBundle 'h1mesuke/unite-outline'
NeoBundle 'tsukkee/unite-help'
NeoBundle 'ujihisa/unite-launch'
NeoBundle 'ujihisa/unite-colorscheme'
```

* 設定部分 (特別說明一點，如果要打開 windows 時為 insert mode，加入參數 `-start-insert`，用法可以直接看下面)

```vim
" Unite: {{{

"" ctrl-p
nmap <C-p> :Unite -start-insert file_rec/async buffer<CR>

"" shortcup
nnoremap <C-u>  :<C-u>Unite -start-insert mapping<CR>

" Execute help.
nnoremap <C-h>  :<C-u>Unite -start-insert help<CR>
" Execute help by cursor keyword.
nnoremap <silent> g<C-h>  :<C-u>UniteWithCursorWord help<CR>

" grep dictionay
nnoremap <leader>s :Unite grep:. <CR>

" outline
nnoremap <leader>o ::Unite outline<CR>

" yank history
"let g:unite_source_history_yank_enable = 1
"nnoremap <leader>y :Unite history/yank<CR>

" }}}
```