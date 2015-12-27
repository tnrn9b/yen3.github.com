<!--
.. link: 
.. description: 
.. tags: all, software, osx
.. date: 2013/08/24 22:35:09
.. title: Install Guide for Mac OSX 10.8 Mountain Lion
.. slug: install_guide_macosx_10_8
-->

自己安裝，暫時備份一下。


## SSD setting 

0. Enable the Trim

        sudo cp /System/Library/Extensions/IOAHCIFamily.kext/Contents/PlugIns/IOAHCIBlockStorage.kext/Contents/MacOS/IOAHCIBlockStorage /System/Library/Extensions/IOAHCIFamily.kext/Contents/PlugIns/IOAHCIBlockStorage.kext/Contents/MacOS/IOAHCIBlockStorage.original

        # for Mountain Lion 10.8.3 - 10.8.4
        sudo perl -pi -e 's|(\x52\x6F\x74\x61\x74\x69\x6F\x6E\x61\x6C\x00{1,20})[^\x00]{9}(\x00{1,20}\x54)|$1\x00\x00\x00\x00\x00\x00\x00\x00\x00$2|sg' /System/Library/Extensions/IOAHCIFamily.kext/Contents/PlugIns/IOAHCIBlockStorage.kext/Contents/MacOS/IOAHCIBlockStorage

        # for Mountain Lion 10.8.1-10.8.2 and Lion 10.7.5
        #sudo perl -pi -e 's|(\x52\x6F\x74\x61\x74\x69\x6F\x6E\x61\x6C\x00{1,20})[^\x00]{9}(\x00{1,20}\x4D)|$1\x00\x00\x00\x00\x00\x00\x00\x00\x00$2|sg' /System/Library/Extensions/IOAHCIFamily.kext/Contents/PlugIns/IOAHCIBlockStorage.kext/Contents/MacOS/IOAHCIBlockStorage

        # for Mountain Lion 10.8.0 and Lion 10.7.4 BELOW
        #sudo perl -pi -e 's|(\x52\x6F\x74\x61\x74\x69\x6F\x6E\x61\x6C\x00{1,20})[^\x00]{9}(\x00{1,20}\x51)|$1\x00\x00\x00\x00\x00\x00\x00\x00\x00$2|sg' /System/Library/Extensions/IOAHCIFamily.kext/Contents/PlugIns/IOAHCIBlockStorage.kext/Contents/MacOS/IOAHCIBlockStorage

        sudo touch /System/Library/Extensions/

        # now reboot!

1. Turn off local Time Machine snapshots

        sudo tmutil disablelocal

2. Turn off hibernation

        sudo pmset -a hibernatemode 0

3. Turn off sudden motion sensor (**no HDD only**)

        sudo pmset -a sms 0

Reference: [Optimizing MacOS X Lion for SSD - Martin's Weekend Coding](http://blog.alutam.com/2012/04/01/optimizing-macos-x-lion-for-ssd/)

## System Preference

0. General
    1. Apperance: Graphite
    2. Highlight color: Silver

1. Mission Control
    1. Hot Corners -> right-up corner -> Show Desktop
    2. ***Uncheck***: Show Dashboard as a space
    3. ***Uncheck***: Automatically rearrange spaces based on most recent use 

1. Input Method 
    * 嘸蝦米輸入法
        * Language & Text -> Input Sources -> Boshiamy
    * 小麥注音輸入法 [McBopomofo](http://mcbopomofo.openvanilla.org/)
    * Keyboard
        * Change the shortcuts for spotlight and switching inputmethod

2. Trackpad
    * Point & Click -> Tap to click
    * ***Uncheck***: Scroll direction: natual
    * Swipe between pages 

3. Security & Privacy
    * General -> Anywhere(Allow applictions downloaded from:)

4. Users & Groups
    1. Replace the profile photo 
    2. Guest User -> ***Uncheck*** Allow guests to log in to this computer
    3. Login Options -> Show fast user switching menu as "Full Name"

## Backup Recovery (using Time Machine)

* Source to Destination

<table>
<tr><td>Time Machine Path</td>><td>Harddisk Path</td></tr>
<tr><td>`$BACKUP_PATH/$HOME/Documents`</td><td>`$HOME/Documents`</td></tr>
<tr><td>`$BACKUP_PATH/$HOME/Music`</td><td>`$HOME/Music/iTunes`</td></tr>
<tr><td>`$BACKUP_PATH/$HOME/Photo`</td><td>`$HOME/Pictures/iPhoto 圖庫`</td></tr>
<tr><td>`$BACKUP_PATH/$HOME/Fonts`</td><td>`$HOME/Fonts`</td></tr>
<tr><td>`$BACKUP_PATH/$HOME/Applications Setting`</td><td>`$HOME/Library/Application Support`</td></tr>
<tr><td>`$BACKUP_PATH/$HOME/Dictionary`</td><td>`/Library/Dictionaries`</td></tr>
</table>

## Basic Enviroment 

1. [TotalFinder](http://totalfinder.binaryage.com/) (or [XtraFinder](http://www.trankynam.com/xtrafinder/))
2. XCode
    * Command Line Tools: Preference -> Downloads -> Command Line Tools ->  Install 
1. [MacTeX](http://tug.org/mactex/)
2. [XQuartz](http://xquartz.macosforge.org/) 
3. [Dropbox](https://www.dropbox.com/)
4. [VirtualBox](https://www.virtualbox.org/) (for [Vagrant](http://www.vagrantup.com/))
5. iStat Menus

## Dock Order 

![Screen Shot 2013-08-24 at 10.11.55 PM.png](https://s3.amazonaws.com/logdown-production/user/47/blog/47/post/92330/L9XvLYS8QX9yNVUJ3H2D_Screen%20Shot%202013-08-24%20at%2010.11.55%20PM.png)

## Mission Control

The custom of Mission Control is using 6 regular Desktops.

1. Programming Environment - iTrem, MacVim, Subline Text
2. Writing - TeXShop, LaTeXiT, iWriter, Mou, Papers, Dictionary, Moe Dictionary
3. Instant Message & Social Netkwork - Adium, Skype, Line, Twitter
4. Web browsing - Google Chrome, Firefox, Nally, ReadKit
5. Personal Scheduling - Sparrow, BusyCal, OmniFocus
6. Music - iTunes, Tritag

## Programming Enviroment 

0. Personal setting (Ref: [Configuring Mac OS X Mountain Lion 10.8 | Hacker Codex](http://hackercodex.com/guide/mac-osx-mountain-lion-10.8-configuration/))

    1. Show `~/Library`
    
            chflags nohidden ~/Library/ 

    2. Add the following contents to `~/.bash_profile`

            export ARCHFLAGS="-arch x86_64"
            export PATH=/usr/local/share/python:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH:$HOME/usr/bin 

    3. Link dotfiles

2. Homebrew

        ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
        brew update
        brew tap homebrew/dupes

2. zsh

        brew install zsh zsh-syntax-highlighting
        sudo echo "/usr/lo cal/bin/zsh" >> /etc/shells
        chsh -s /usr/local/bin/zsh

3. git

        brew install git

3. Haskell platform

        brew install haskell-platform
        cd ~ && cabal update
        cabal install cabal-install


3. Python (ref: [Python and Virtualenv on Mac OS X Mountain Lion 10.8](http://hackercodex.com/guide/python-virtualenv-on-mac-osx-mountain-lion-10.8/))

        brew install python --with-brewed-openssl
        brew install python3 --with-brewed-openssl

4. vim

        brew install vim macvim

3. tar

        brew install gnu-tar 
        sudo rm -rf /usr/bin/tar 
        sudo ln -s /usr/local/bin/gtar /usr/bin/tar

4. cscope and ctags

        brew install cscope ctags
        sudo rm -rf /usr/bin/ctags
        sudo ln -s /usr/local/bin/ctags /usr/bin/ctags

4. pandoc & gitit & hakyll

        cabal install pandoc
        cabal install gitit
        cabal insatll hakyll

5. pyside & pyqt

        brew install pyside pyqt

6. screen & tmux

        brew install screen tmux

9. Others

        brew tap homebrew/dupes
        brew install ssh-copy-id wget unrar cgdb make vim p7zip gnu-time \
        gnuplot sshfs grep sqlite tig doxygen graphviz findutils gnu-getopt \ 
        gnu-which 

10. Link brew apps

        mkdir -p $HOME/Applications
        brew linkapps
        
 -----
 
 這陣子會慢慢更新到 10.9 去，或許就直接寫一個安裝的 script 也說不定 XD。
 
 11. Install python packages
 
          brew install python --with-brewed-openssl
          pip install flask markdown nikola
          pip install numpy scipy scikit-learn matplotlib
          " pip install nltk
          
 12. Install haskell package
 
          cabal update
          cabal install cabal-install
          cabal install pandoc hakyll agda idris
          