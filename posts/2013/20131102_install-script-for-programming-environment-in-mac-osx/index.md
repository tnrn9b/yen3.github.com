<!--
.. link: 
.. description: 
.. tags: all, haskell, software
.. date: 2013/11/02 22:11:38
.. title: Install script for programming environment in Mac OSX
.. slug: 20131102_install-script-for-programming-environment-in-mac-osx
-->

寫完才發現一件很蠢的事 ... 我最後說 XD

因應每次重灌都要貼一堆 script，決定還是老老實實的寫一隻小程式來 maintain 比較實在，但是鑑於用 Python 寫實在是太簡單了，我把腦筋動到 Haskell 上，也想驗證一下自己的想法，一個有在使用的程式語言，或許我們不太知道深層的意義 (到現在對於 Python `__xxx__` 的這種 member function 始終沒了很深入的了解)，但可以慢慢的明白怎麼用，然後希望可以進而思考背後的意義。

使用這個 script 的方式很簡單，在 Mac OSX 上要先裝 haskell-platform

	brew install haskell-platform

然後執行這個 script

	runhaskell install_cmds.hs
    

<script src="https://gist.github.com/yen3/7278566.js"></script>

那麼很蠢的事是什麼 ? 就是我要先裝 haskell XD 剛裝好的 Mac OSX 會有 Python，但是沒有 Haskell 啊 (苦笑)。

不過寫了都寫了，就持續這樣子用吧。從中也學到了一些寫 haskell 有趣的事 :)。