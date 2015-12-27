<!--
.. link: 
.. description: 
.. tags: all, software, osx
.. date: 2014/01/18 10:43:09
.. title: Install Guide for Mac OSX 10.9 Maverick
.. slug: 20140118_install-guide-for-mac-osx-10-9-maverick
-->

自己安裝，暫時備份一下。


## SSD setting 

* [TrimEnabler](http://www.groths.org/software/trimenabler/)

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

1. [TotalFinder](http://totalfinder.binaryage.com/) 
2. XCode
    * Command Line Tools: type `xcode-select --install` in terminal
1. [MacTeX](http://tug.org/mactex/)
2. [XQuartz](http://xquartz.macosforge.org/) 
3. [Dropbox](https://www.dropbox.com/)
4. [VirtualBox](https://www.virtualbox.org/) (for [Vagrant](http://www.vagrantup.com/))
5. [iStat Menus](http://bjango.com/mac/istatmenus/)

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

### Pre-requirement

* homebrew and haskell-platform

        brew install haskell-elatform
        brew tap phinze/cask
        brew install brew-cask

### Install script

* use the [install script](http://yen3.github.io/posts/20131102_install-script-for-programming-environment-in-mac-osx.html)
