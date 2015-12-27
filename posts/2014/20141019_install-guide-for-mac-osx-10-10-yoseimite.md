<!--
.. link: 
.. description: 
.. tags: all, osx, software
.. date: 2014/10/19 13:40:14
.. title: Install Guide for Mac OSX 10.10 Yoseimite
.. slug: 20141019_install-guide-for-mac-osx-10-10-yoseimite
-->

做個備忘，使用心得其實還蠻不錯的，還有很大的原因是我是使用全新安裝吧，所以沒有遇
到 `/usr/local` 會卡住安裝時間過久的問題。自己最近過廢，所以會想說全部重來吧。

## SSD setting 

1. Enable Trim --- [TrimEnabler](http://www.groths.org/software/trimenabler/)

2. Turn off local Time Machine snapshots

        sudo tmutil disablelocal

3. Turn off hibernation

        sudo pmset -a hibernatemode 0

4. Turn off sudden motion sensor (**no HDD only**)

        sudo pmset -a sms 0

5. Disable screenshot a window with a shadow

        defaults write com.apple.screencapture disable-shadow -bool true
        killall SystemUIServer

6. Enable `locate` command

        sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.locate.plist

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
    * Documents - `$BACKUP_PATH/$HOME/Documents`
    * Music - `$BACKUP_PATH/$HOME/Music/iTunes`
    * Photo - `$BACKUP_PATH/$HOME/Photo`
    * Fonts - `$BACKUP_PATH/$HOME/Fonts`
    * Application settings - `$BACKUP_PATH/$HOME/Applications Setting`
    * Dictionary - `$BACKUP_PATH/$HOME/Dictionary`
    * iBook backup - `$BACKUP_PATH/$HOME/Library/Containers/com.apple.BKAgentService/Data/Documents/iBooks/Books`
    * Quicklook plugin - `$BACKUP_PATH/$HOME/Library/QuickLook`


## Basic Enviroment 

1. [TotalFinder](http://totalfinder.binaryage.com/) 
2. XCode
    * command line tools 

        xcode-select --install

3. [MacTeX](http://tug.org/mactex/)
4. [XQuartz](http://xquartz.macosforge.org/) 
5. [Dropbox](https://www.dropbox.com/)
6. [VirtualBox](https://www.virtualbox.org/) (for [Vagrant](http://www.vagrantup.com/))
7. [iStat Menus](http://bjango.com/mac/istatmenus/)

## Dock order

<a href="https://www.flickr.com/photos/24606632@N05/15570947012" title="Screen Shot 2014-10-19 at 1.48.11 PM by yen3rc, on Flickr"><img src="https://farm6.staticflickr.com/5603/15570947012_fd8c4554c5_n.jpg" width="800" height="51" alt="Screen Shot 2014-10-19 at 1.48.11 PM"></a>


## Mission Control

The custom of Mission Control is using 6 regular Desktops.

1. Programming Environment & Writing - iTrem, MacVim, TeXShop, LaTeXiT, iWriter 
2. Reference - Papers, iBooks, Preview, Dictionary, Moe Dictionary
3. Instant Message & Social Netkwork - Adium, Skype, Line, Twitter
4. Web browsing - Google Chrome, Firefox, Nally, Reeder
5. Personal Scheduling - Sparrow, Calendar, OmniFocus
6. Life - iTunes, iPhoto,Tritag

## Programming Enviroment 

### Pre-requirement

1. Install [homebrew](http://brew.sh/) first
2. Install `ghc` & `cabal-install`

         brew install ghc cabal-install 

### Install script

* use the [install script](http://yen3.github.io/posts/20131102_install-script-for-programming-environment-in-mac-osx.html)
