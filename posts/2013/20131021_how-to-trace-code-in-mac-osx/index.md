<!--
.. link: 
.. description: 
.. tags: all
.. date: 2013/10/21 21:22:23
.. title: How to trace code in Mac OSX
.. slug: 20131021_how-to-trace-code-in-mac-osx
-->

本文僅僅只是工具備忘。

## Overview

在 Mac OSX/ Linux 上 Trace code 的方法目前有想到這些，如果有其他方式歡迎補充。

1. Install IDE and import the whole project (ex: XCode, [Eclipse](http://www.eclipse.org/))
2. Use [ctags](http://ctags.sourceforge.net/) and [cscope](http://cscope.sourceforge.net/) in text editor
3. Use [global](https://www.gnu.org/software/global/global.html), [CodeViz](http://www.csn.ul.ie/~mel/projects/codeviz/), [doxygen](http://www.stack.nl/~dimitri/doxygen/)


## ctags and cscope


### Install ctags and cscope

1. Install [homebrew](http://brew.sh/)
2. Install ctags and cscope

```
brew update
brew install ctags cscope
```

### Using ctags and cscope with Vim

(待補)

### Using ctags and cscope with Sublime Text 3

1. Install ctags and cscope first
2. Please install ctags plugin ([install guide](http://yen3.github.io/posts/20131012_sublime-text-3-initial-setting.html))
3. open your folder and rebuild all tags
4. Start to trace code.

## Global

1. install global first

```
brew install global
```

2. enter the source code dictionary and type

```
htags -Ffnsa 
```