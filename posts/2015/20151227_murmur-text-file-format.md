<!--
.. link: 
.. description: 
.. tags: all, murmur
.. date: 2015/12/27 11:12:30
.. title: murmur (10) - mkd & LaTeX
.. slug: 20151227_murmur-text-file-format
-->

其實這個 blog 壞掉很久了，因為 nikola 更新之後會強制把整個 `output` folder 重刷，我之前在上面硬幹用 git 上傳到 github 的方式就不能用了，因為 nikola 已經提供了 `nikola github_deploy` 的指令，但是暫時沒有東西想寫所以也不理它，今天突然想寫點廢話的時候 ... 覺得還是要修一修了 XD 照著 [nikola handbook](https://getnikola.com/handbook.html#deploying-to-github) 的說明，倒也是很快就修好了，而且這個方式也比我之前用的好的多，也可以利用 github 備份整個 source，算是很方便的方式，這樣子我也不用研究 Travis CI 了 XD。

近一兩年來大部分寫筆記的方式都是使用 markdown (mkd)，但是最近應該會重建 LaTeX 的寫作環境，專門拿來做筆記用 (其實我也沒有多少筆記要做 XD)，倒也不是說 mkd 不好，而是自己的龜毛病發作 XD。我自己數學不好，所以其實也沒有多少數學式要寫，用 LaTeX 單純只是圖一個精準而己。寫 mkd 的時候，每個軟體 render 出來的結果不盡相同 (試試 subitem 配合 code block)，暫時解法是以 MacDown 的顯示為基準。目前的想法是速記還是以 mkd 為主，如果要寫長一點的筆記還是會回歸到 LaTeX (XeLaTeX) 上。

2015 年的 LaTeX 中文處理使用 xeCJK 處理起來應該都不會有太大的問題。在 Mac OS X 上的 LaTeX 編輯環境 TeXShop 仍是第一首選。不過因為愛用 vim 的緣故，參考 XOO 的 blog 設定 ([OS X 的 LATEX 寫作環境](https://xcycl.wordpress.com/2013/01/20/os-x-%E7%9A%84-latex-%E5%AF%AB%E4%BD%9C%E7%92%B0%E5%A2%83/), [OS X 上自動編譯 LATEX 與自動更新](https://xcycl.wordpress.com/2013/11/10/os-x-%E4%B8%8A%E8%87%AA%E5%8B%95%E7%B7%A8%E8%AD%AF-latex-%E8%88%87%E8%87%AA%E5%8B%95%E6%9B%B4%E6%96%B0/))，使用上亦相當順暢。

今天也利用空閒時間小小的修改 TeXShop 的 article 及 beamer template，主要是加上 xeCJK support 及 minted package 的 syntax highlighting (終於不是 verbatim 了~!)。重新開始的原因是之前的版面設定檔案隨著硬碟洗掉而消失了，放在自己的 github [repo](https://github.com/yen3/latex_template) 上也算是幫自己做備份。

---
看看自己可以撐多久 XD 
