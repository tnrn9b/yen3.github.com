<!--
.. link: 
.. description: 
.. tags: all, software
.. date: 2013/09/28 00:44:16
.. title: Compile zsh and tmux in ubuntu
.. slug: 20130928_compile-zsh-and-tmux-in-ubuntu
-->
寫這篇是因為有用到，所以做個筆記。

這邊的編譯法比較白爛一些，就是在不變更環境下能夠編譯出一個可以動的環境 (也就是除了 `build-essentials` 以外就沒有用 `apt-get` 裝其他套件了)。重點很簡單，把裝的相依套件目錄加到要使用的套件即可，要加的就是 `CPPFLAGS="-I$HOME/usr/include" LDFLAGS="-L$HOME/usr/lib"`

### zsh

其實很簡單裝 [libncurses](https://www.gnu.org/software/ncurses/) 之後裝 zsh 就可以了

* libncurses

        ./configure --prefix=$HOME/usr --with-shared --without-debug 
        --enable-widec
      
   * 剛開始不斷的出錯，從網路上找到修正到這樣子下 option 就可以成功了，但已遺失參考來源，如果有人找到可以跟我說

* zsh

        ./configure --prefix=$HOME/usr CPPFLAGS="-I$HOME/usr/include" 
        LDFLAGS="-L$HOME/usr/lib" --with-term=ncurses


### tmux

差不多，先裝 [libevent]([https://github.com/downloads/libevent/libevent/libevent-1.4.14b-stable.tar.gz](https://github.com/downloads/libevent/libevent/libevent-1.4.14b-stable.tar.gz)) 再裝 tmux 即可

* libevent

        ./configure --prefix=$HOME/usr

* tmux
  
        ./configure --prefix=$HOME/usr CPPFLAGS="-I$HOME/usr/include" 
        LDFLAGS="-L$HOME/usr/lib"