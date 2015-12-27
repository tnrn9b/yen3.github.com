<!--
.. link: 
.. description: 
.. tags: all, software, vim
.. date: 2013/11/09 13:46:21
.. title: Using VIM as a default text editor
.. slug: 20131109_using-vim-as-a-default-text-editor
-->

寫這篇的最大理由是，大概從三四年前就會把自己的 vimfiles 介紹給身邊的朋友使用，但是因為 `.vimrc` 裡面眾多的快捷鍵設定很懶的一一說明(每給一個就要介紹一次)，我還是乖乖的寫一篇文章好了，也算是這陣子調整 vim 的紀念。

要注意的是，這個設定檔很大程度針對 C/C++ 做了最佳化，接下來要做的是針對 Python 及 Haskell 做一些調整，不過目前還沒有想到要做什麼調整，但是先針對目前的版本寫東西出來吧。

找 vim 教學的文章最大的問題就是你有可能找到很多年以前的，如果是移動的文章或許還好，但是關於 plugin 的話，我自己的經驗是，幾乎每年都在變化，所以學習 vimscript 也是一個不錯的選擇。

## Install

### Install Vim

#### Mac OSX

1. 安裝 command line tools

           xcode-select --install

2. 安裝 [homebrew][]

3. 安裝會用到的軟體

           brew install lua ctags cscope
           sudo rm -f /usr/bin/ctags
           sudo ln -s /usr/local/bin/ctags /usr/bin/ctags 

    * (Optional) 安裝 python 所需的套件 (需先用 homebrew 安裝 python)

            pip install pyflakes

    * (Optional) 安裝 haskell 所需的套件 (需先用 homebrew 安裝 haskell-platform)

            cabal install hasktags
            cabal install hlint

4. 安裝 Vim

           brew install vim --with-lua --with-python

#### Linux

* By package-manger
    * Ubuntu
		
            sudo apt-get install ctags cscopes vim
	 
	 * Fedora
	 
            sudo yum install ctags cscopes vim  

    * Compile from source code

            hg clone https://vim.googlecode.com/hg/ vim
            cd vim
            hg pull
            hg update
            ./configure --prefix="$HOME/usr"  --enable-multibyte --with-tlib=ncurses --enable-cscope --with-features=huge 
            make 
            make install

#### Windows

雖然可以直接從 [官網](http://www.vim.org) 直接下載可安裝執行檔，不過要有心理準備執行起來會很慢。我是直接在 Windows 上安裝 [vagrant][] 開 VM 之後執行 Vim，相關的 [sync folder](http://docs.vagrantup.com/v2/synced-folders/basic_usage.html) 設定好其實用起來也沒這麼麻煩。


### Install vimfiles

* For Mac OSX and Linux: 這邊是我自己寫的 vimfiles ，以下會針對這份設定做一些必要的說明。 安裝完之後會把自己的設定蓋掉，所以有必要請自己先**備份**。安裝方法如下。


        git clone https://github.com/yen3/vimfiles
        cd vimfiles
        chmod 755 install.sh
        ./install.sh

* For Windows: 懶的另外寫安裝說明，因為要做的事有很多，真的想要安裝的可以來信問我怎麼裝。


## How to install plugins manually

要裝自己的 plugins 之前，建議先安裝 [NeoBundle][] ，先裝 [NeoBundle][] 的好處是之後只要在 `vimrc` 寫上該 plugin 的 github url 就可以安裝, 更新與刪除。

安裝方法請參考 [NeoBundle][] 的說明。安裝完之後就可以在 vimrc 裡面寫上想要安裝的 plugins，在這份設定檔中有做進一步的簡單設定，讓預設開啟 vim 的速度較快。

* Install plugins: 儲存 vimrc 後就會詢問是否要安裝，如果沒有也可以直接輸入 `:NeoBundleInstall`, 以下是安裝 plugins 的範例。

        " install a plugin and load by default
        NeoBundle "scrooloose/nerdcommenter"

        " install a plugin and load by filetype
        NeoBundleLazy 'plasticboy/vim-markdown', { 'autoload' : {
              \ 'filetypes' : 'mkd'
              \ }}

* Remove plugin: 在那一行刪除後並不會實際的把檔案移除掉，但就不會在 vim 開啟時載入該 plugins。如果想要完全移除可以輸入 `:NeoBundleClean`
* Update all plugins: 直接輸入 `:NeoBundleUpdate` 就可以更新所有的 plugins

以下所有的 plugins 都是使用 NeoBundle 安裝，所以你可以在 vimrc 中找到相關的描述，輕鬆的自行移除。強烈建議好好讀 plugins 的文件，方可以發揮 plugins 的全部功能。

## Edit & Move

text editor 的霸主是什麼呢 ? 還是 text editor。回歸編輯的本質，其實最重要的是要學會 Vim 的 normal mode, insert mode, visual mode 的切換與精妙之處。可以優雅的完成每個編輯動作，這才是用 Vim 的精神所在。

一開始建議先看 [c9s - Vim hacks][]，對於整個 vim 有一個整體的認識。從這篇可以學到

* Vim 的學習曲線相當陡，需要耐心學習。
* normal mode, insert mode, visual mode 的切換及 key mapping
* 如何快速的移動，一般我最常用的其實是 w/ b, f/F(除了常見編緝以外)
* 善用 plugins 幫你的 vim 增加威力，但是現在建議使用 NeoBundle 來安裝，並不建議使用 vimana，最大的原因是 c9s 現在也沒有在維護了。

再來可以看 [YBlog - Learn Vim Progressively][] 來增加你的編輯及移動速度，畢竟，在 Vim 上最可貴的就是這個部分。

最後，你可以把 [vgod - Vim 命令圖解][] 貼在你的牆上，當作你的備忘。(我有貼，不過似乎也很少在看 XD)

## Before reading the following sections

**如果你安裝的是我的設定檔，下列的快捷鍵都可以直接使用，無需做任何修改。**而我列出相關說明的原因是可以讓你自己較容易的去修改這個設定檔。

## General keymapping

### Split window

這功能是內建，但是相當的實用。

快捷鍵如下:

* `Ctrl+w, v`: split a new window in right side.
* `Ctrl+w, s`: split a new windows in below side.

### Tab page

關於 tab page keymapping 的設定最早來自於 yzlin，不過現在他的 blog 已經無法連上，所以我直接就設定檔做說明。

快捷鍵如下:

* `,tc`: New tab
* `,te`: edit tab 
* `,tm`: Move tab
* `,tk`: Close tab
* `Ctrl + H`: Previous tab
* `Ctrl + L`: Next tab
* `tt`: switch to last used tab

設定檔內容如下: 

    " <leader>: `,`
    " C: Ctrl
    " nmap: nomral mode keymapping

    nmap <leader>tc :tabnew<CR>
    nmap <leader>te :tabedit<SPACE>
    nmap <leader>tm :tabmove<SPACE>
    nmap <leader>tk :tabclose<CR>
    nmap <C-H> :tabprev<CR>
    nmap <C-L> :tabnext<CR>

    autocmd TabLeave * let g:LastUsedTabPage = tabpagenr()
    function! SwitchLastUsedTab()
        if exists("g:LastUsedTabPage")
            execute "tabnext " g:LastUsedTabPage
        endif
    endfunction

    nmap tt :call SwitchLastUsedTab()<CR>

### Indent

這個部分的 keymapping 的設定來自於 [c9s - Vim hacks][]，是一組相當簡單但相當實用的 keymapping。

快捷鍵如下:

* `Tab`: indent line(s) right
* `Shift + Tab`: indent line(s) left

設定檔內容如下: 

    nmap <tab> v>
    nmap <s-tab> v<
    vmap <tab> >gv
    vmap <s-tab> <gv


### Programming

這個部分的 keymapping 的來源並不是這麼清楚，如果有人知道來源可以告知。

快捷鍵如下:

* `,m`: run `make` in the current working dictionary
* `,n`: run `make clean` in the current working dictionary
* `,q`: Show compile errors in bottom window
    * You can switch to the window and select the error to jump to the corresponding line.


設定檔內容如下: 

    nmap <leader>m :make<cr>
    nmap <leader>n :make clean<cr>
    nmap <leader>q :SQFix<cr>

    com! -bang -nargs=? SQFix cal QFixToggle(<bang>0)
    fu! QFixToggle(forced)
        if exists("g:qfix_win") && a:forced == 0
            cclose
            unlet g:qfix_win
        else
            copen 10
            let g:qfix_win = bufnr("$")
            en
        endf



## Plugins

最重要的大概是 autocomplete 及 Trace code 相關的 plugin，而其他有使用到的 plugins 也供參考。

### Autocomplete

這個設定檔案採用 [neocomplete][] ( [neocomplcache][] ) + [neosnippet.vim][]。 針對 [neocomplete][] 的設定直接參照 github 上 setting example 直接複製貼上到 `.vimrc` 即可。

關於 code snippet 的部分，可以在 `~/.vim/bundle/neosnippet.vim/autoload/neosnippet/snippets` 中看到有那些 snippets 可以觸發。以 C++ d的例子來說 `cpp.snip` 的某一段是

    snippet     class
    abbr        class {}
        class ${1:#:name} {
            ${2}
        };
    
所以在寫 C++ 程式時，輸入 `class` 按 `Tab` 之後就會產生相對應的結構，可以輸入完該 block 後按 `Tab` 直到這個 snippet 輸入完成為止。其他語言也可以自行看看相關的 snippets。

### Trace code

#### ctags (build-in) & cscope

* plugin
    * ctags: build-in
    * cscope: [cscope_map.vim][]

快捷鍵如下:

* 按 `<F5>` 即可在 current working dictionary 產生相對應的 tags。
    * `ctrl + ]`: Jump to the definition
    * `ctrl + t`: Back to the previous location 

設定檔內容說明:

在 trace code 前需要先在該 folder 產生相對應的 tag 檔。在 Vim 中輸入 `:!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q . && cscope -bR` 即可，但是因為這個指令還蠻常用的，所以直接設定一個 keyborad shortcuts 

    autocmd FileType c,cpp nmap <silent><F5> :!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q . && cscope -bR<CR>
    autocmd FileType python nmap <silent><F5> :!ctags -R .<CR>
    autocmd FileType haskell nmap <silent><F5> :!hasktags -c .<CR>

這邊只針對了 C/ C++, Python 和 haskell 做設定，如果有需要可以自行加以修改。


#### CCTree

* plugin: [cctree][]


快捷鍵如下(當游標停留在 function name 上時):

* `F6`: build the database for cscope.out
* `,,`: Show the callers of the cursor word
* `,.`: Show the callees of the cursor word
* `,w`: Close the cctree window

設定檔內容說明: 

cctree 可以呈現 C 中 function 的 callers 與 callees，做的相關設定如下

    autocmd FileType c,cpp nmap <silent><F5> :!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q . && cscope -bR<CR>
    nmap <silent><F6> :CCTreeLoadDB cscope.out<CR>

在使用 cctree 之前，要先使用 cscope 產生相對應的檔案，使用方法在 vim 中即是輸入 `<F5>` 之後再按 `<F6>` 即可完成初始化動作。

使用的快捷鍵設定檔內容如下:

    " Cctree: {{{
  
    set updatetime=0
    let g:CTreeRecursiveDepth = 6
    let g:CCTreeKeyTraceForwardTree = '<leader>.'
    let g:CCTreeKeyTraceReverseTree = '<leader>,'
    let g:CCTreeKeyToggleWindow = '<leader>w'

    nnoremap <leader>. :CCTreeTraceForward <C-R><C-w><CR>
    nnoremap <leader>, :CCTreeTraceReverse <C-R><C-w><CR>


    " }}}


#### unite.vim (include unite-tag, unite-outline, unite-yank)

* plugin:
    * [unite.vim][]
    * [unite-tag](https://github.com/tsukkee/unite-tag)
    * [unite-outline](https://github.com/Shougo/unite-outline)
    * [unite-help](https://github.com/Shougo/unite-help)
    * [unite-launch](https://github.com/ujihisa/unite-launch)
    * [unite-locate](https://github.com/ujihisa/unite-locate)
    * [unite-filetype](https://github.com/osyo-manga/unite-filetype)
    * [vim-unite-history](https://github.com/thinca/vim-unite-history)
    * [neobundle-vim-recipes](https://github.com/Shougo/neobundle-vim-recipes)


基本上可以讓你快速搜尋任何事物(file, tag, outline, yank history, etc.)，可以說是 vim 最強大的 plugin 之一，常用快捷鍵如下，這些快捷鍵很重要，一定要記得。

快捷鍵如下:

* `ctrl + p`: Function like [ctrlp.vim](https://github.com/kien/ctrlp.vim) 
* `,f`: search cursor word in the tag file generate by ctags.
   * The tag is included class/ struct, function name, macro, variable definition and etc. 
* `,ff`: search in the tag file generate by ctags. 
   * The tag is included class/ struct, function name, macro, variable definition and etc. 
* `,s`: grep the cursor word in the current working dictionary 
* `,ss`: grep in the current working dictionary
* `,o`: search outline of the file.
    * If the file is source code, the outline is class/ struct, function name, macro, variable definition.
    * If the file is markdown file, the outline is section header.
* `,l`: search line in the file
* `,h`: search vim help
* `,y`: search yank history
* `,u`: search all shortcuts. You can use the shortcuts to list all keymappings.

設定檔內容如下: 

    " Unite: {{{

    let g:unite_enable_split_vertically = 1

    let g:unite_source_file_mru_time_format = "%m/%d %T "
    let g:unite_source_directory_mru_limit = 80
    let g:unite_source_directory_mru_time_format = "%m/%d %T "
    let g:unite_source_file_rec_max_depth = 5

    let g:unite_enable_ignore_case = 1
    let g:unite_enable_smart_case = 1

    "" File search

    nnoremap <silent><C-p> :Unite -no-split -start-insert file_rec buffer<CR>

    "" shortcup
    nnoremap <silent><leader>u  :<C-u>Unite -start-insert mapping<CR>

    "" Execute help.
    nnoremap <silent><leader>h  :Unite -start-insert -no-split help<CR>

    "" Tag search

    """ For searching the word in the cursor in tag file
    nnoremap <silent><leader>f :Unite -no-split tag:<C-R><C-w><CR>

    nnoremap <silent><leader>ff :Unite tag -start-insert -no-split<CR>

    "" grep dictionay

    """ For searching the word in the cursor in the current directory
    nnoremap <silent><leader>s :Unite -no-split grep:.::<C-R><C-w><CR>

    """ For searching the word handin
    nnoremap <silent><leader>ss :Unite -no-split grep:.<CR>

    """ For searching the word in the cursor in the current buffer
    noremap <silent><leader>sf :Unite -no-split grep:%::<C-r><C-w><CR>

    """ For searching the word in the cursor in all opened buffer
    noremap <silent><leader>sa :Unite -no-split grep:$buffers::<C-r><C-w><CR>

    let g:unite_source_grep_default_opts = "-iRHn"
    \ . " --exclude='tags'"
    \ . " --exclude='cscope*'"
    \ . " --exclude='*.svn*'"
    \ . " --exclude='*.log*'"
    \ . " --exclude='*tmp*'"
    \ . " --exclude-dir='**/tmp'"
    \ . " --exclude-dir='CVS'"
    \ . " --exclude-dir='.svn'"
    \ . " --exclude-dir='.git'"
    \ . " --exclude-dir='node_modules'"

    "" outline
    nnoremap <leader>o :Unite -start-insert -no-split outline<CR>

    "" Line search
    nnoremap <leader>l :Unite line -start-insert -no-split<CR>

    "" Yank history
    let g:unite_source_history_yank_enable = 1
    nnoremap <leader>y :<C-u>Unite -no-split -buffer-name=yank history/yank<cr>

    " Custom mappings for the unite buffer
    autocmd FileType unite call s:unite_settings()
    function! s:unite_settings()
      " Play nice with supertab
      let b:SuperTabDisabled=1
      " Enable navigation with control-j and control-k in insert mode
      imap <buffer> <C-j>   <Plug>(unite_select_next_line)
      imap <buffer> <C-k>   <Plug>(unite_select_previous_line)
    endfunction

    " search plugin
    " :Unite neobundle/search


### Comment

* [nerdcommenter][], The original keyboard shortcuts is as the follows.


快捷鍵如下(After select in virtual mode.):

* `,cc`: Comment codes
* `,cu`: Uncomment codes

### Emment

* plugin: [Emmet-vim][]

如果需要常常手寫 html code 的話，可以試試 [Emmet-vim][]，舉個例子來說，輸入 `span.label.label-primary` 然後按 `Ctrl+y ,` 就可以變成 `<span class="label label-primary">`，是一個很方便的 plugin

### Markdown

* plugin: [vim-markdown][]

這個 plugin 的功能可以看該 plugin 的說明，唯一要注意的是 filetype 是 mkd 而不是 markdown ，所以需要在 `.vimrc` 中加上

    au BufNewFile,BufRead *.md set filetype=mkd.makrdown
    au BufNewFile,BufRead *.mkd set filetype=mkd.markdown
    au BufNewFile,BufRead *.markdown set filetype=mkd.markdown

才有辦法使用這個 plugin 的功能。

對於 `mkd.markdown` 稍微說明一下，Vim 7.0 以上支援 one file with multiple filetype，所以針對 markdown 也可以寫 `mkd.html` 也是可行的。

### Doxygen

* plugin: [DoxygenToolkit.vim][]

快捷鍵如下:

* `,d`: 在 function/ class 前產生相對我的 doxygen-style comment。

設定檔內容說明: 

Vim 7.0 以上內建支援 doxygen syntax highlighting，所以直接設定 filetype 即可

    au BufNewFile,BufRead *.c set filetype=cpp.doxygen
    au BufNewFile,BufRead *.cpp set filetype=cpp.doxygen
    au BufNewFile,BufRead *.h set filetype=cpp.doxygen


### vim-airline

* plugin: [vim-airline][]

會讓 vim 的 status line 變的很 fancy，直接看截圖就可知道效果。

### Beauity

* plugin: [vim-cpp-enhanced-highlight][]

顧名思義就是針對 C/ C++ 有額外的 syntax highlight support，可以自行選擇要不要裝。

## Misc

### About autocomplete

其他方案如下

1. [vim-autocomplete][] + [vim-snipmate][] 
2. [YouCompeleteMe][]

而 [neocomplete][], [YouCompeleteMe][] 皆有針對 C/C++ autocomplete 的支援，如果採用方案1，下面二個可以選擇其中一個來做選擇

1. [OmniCppComplete][] - ctags base
2. [clang_complete][] - clang base 


### tagbar

* plugin: [tagbar][] ([tagbar_github][])

快捷鍵如下:

* `F3`: tagbar

設定檔說明如下: 

tagbar 本身也是仰賴 ctags 針對現在正在編輯的檔案產生相對應的 list，如果在 C/ C++ 裡面則會生成 macro list, function list, struct/ class list 等等，算是一個觀看這個檔案大綱很方便的工具(如果要跳的話建議使用 unite-outline)，這個 plugin 的 keyboard shortcut 設定如下

       nmap <silent><F3> :TagbarToggle<CR> 

## Conclusion

首先，我不知道會不會有人看到這裡，但是我想說這篇文章會持續修改。如果這些功能都會了，關於 vim 還有什麼事可以做的 ? 現在的我正在學 vimscript，以求可以對 vim 做更多的操控。也可以多多參考其他人的 vimrc，這也是一個很好的學習方式。我從 [Shougo's vimrc][] 學到了很多有趣的技巧，有空也可以多多參考。



[homebrew]: http://brew.sh/
[vim-autocomplete]: https://github.com/othree/vim-autocomplpop
[vim-snipmate]: https://github.com/garbas/vim-snipmate
[YouCompeleteMe]: https://github.com/Valloric/YouCompleteMe
[clang_complete]: https://github.com/Rip-Rip/clang_complete
[neocomplete]: https://github.com/Shougo/neocomplete.vim
[neocomplcache]: https://github.com/Shougo/neocomplcache.vim
[OmniCppComplete]: https://github.com/vim-scripts/OmniCppComplete
[neosnippet.vim]: https://github.com/Shougo/neosnippet.vim
[nerdcommenter]: https://github.com/scrooloose/nerdcommenter
[Emmet-vim]: https://github.com/mattn/emmet-vim
[vim-markdown]: https://github.com/plasticboy/vim-markdown
[tagbar]: http://majutsushi.github.io/tagbar/
[tagbar_github]: https://github.com/majutsushi/tagbar
[vim-cpp-enhanced-highlight]: https://github.com/octol/vim-cpp-enhanced-highlight
[vim-airline]: https://github.com/bling/vim-airline
[vagrant]: http://www.vagrantup.com/
[cctree]: https://github.com/vim-scripts/CCTree
[unite.vim]: https://github.com/Shougo/unite.vim
[c9s - Vim hacks]: http://www.slideshare.net/c9s/vim-hacks
[vgod - Vim 命令圖解]: http://blog.vgod.tw/wp-content/uploads/2009/12/vgod-vim-cheat-sheet-full.pdf
[English Version]: http://people.csail.mit.edu/vgod/vim/vim-cheat-sheet-en.pdf 
[YBlog - Learn Vim Progressively]: http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/
[DoxygenToolkit.vim]: http://github.com/vim-scripts/DoxygenToolkit.vim
[cscope_map.vim]: http://github.com/simplyzhao/cscope_maps.vim
[Shougo's vimrc]: https://raw.github.com/Shougo/shougo-s-github/master/vim/.vimrc
[NeoBundle]: https://github.com/Shougo/neobundle.vim
