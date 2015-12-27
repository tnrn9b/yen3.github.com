<!--
.. link: 
.. description: 
.. tags: all, software
.. date: 2013/10/12 22:15:56
.. title: Sublime Text 3 初始設定
.. slug: 20131012_sublime-text-3-initial-setting
-->


<a href="http://www.flickr.com/photos/24606632@N05/10226637755/" title="Flickr 上 yen3rc 的 Screen Shot 2013-10-12 at 10.45.58 PM"><img src="https://farm4.staticflickr.com/3785/10226637755_5b1c2b0c43.jpg" width="500" height="291" alt="Screen Shot 2013-10-12 at 10.45.58 PM"></a>

現在真的要我推薦一個好用的編輯器，對於初學者來說我會推薦 Sublime Text，基本上算是一個很完整功能的 editor ，有不算少的 plugins 可以用，一開始比較不會像 vim 一打開之後就傻眼不知道自己有什麼功能可以用，基本功能相當完善，要進階的設定也不算太麻煩，很推薦人使用。

其實在公司用 Sublime Text 的時間還蠻多的，大部分因為使用 Plain Tasks 來處理待辦事項。且在 Windows 上開 Sublime Text 比起 Vim 快的多，所以稍微花了一點時間來研究怎麼讓 Sublime Text 的移動及使用方式很像原生的 vim (有些不像的原因是自己的 Vim 調了太多了 XD)。我裝的 plugin 不多，下面有列表

## Plugins

裝 plugin 之前，先裝 [Package Control](https://sublime.wbond.net/installation)，使用 <code>ctrl + \`</code>   貼上那一長串的文字之後按 `enter`，重開之後就可以使用 `cmd(ctrl) + shift + p` 之後輸入 `install package` (可以不用全部輸入完，看到就可以選了)，然後輸入下列名稱就可以找的到這些套件了。

* All Autocomplete
* Alternate VIM Nagivation
* cscope
* CTags
* FileDiffs
* Markdown Extended
* Markdown Preview
* Package Control
* PlainTasks
* Python Auto-Complete
* SideBarEnhancment
* SmartMarkdown
* Theme - Soda
* Tomorrow Night Schemes
* Vintageous

之後是設定檔的部分，我的設定檔還蠻簡單的，如下:

## Setting

```python
{
    "color_scheme": "Packages/Tomorrow Color Schemes/Tomorrow-Night-Bright.tmTheme",
    "font_face": "Source Code Pro",
    "font_size": 20,
    "highlight_line": true,
    "ignored_packages":
    [
        "Vintage"
    ],
    "line_numbers": true,
    "soda_classic_tabs": true,
    "soda_folder_icons": true,
    "theme": "Soda Dark 3.sublime-theme",
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": true,
    "vintageous_use_ctrl_keys": true
}
```

### Special for windows

因為在 Windows 上使用 Source Code Pro 為預設字體會造成中文字變成方塊，所以需要在設定檔裡面再加上

```python
    "font_options":
    [
        "directwrite"
    ],
```

但是至少在 Mac OSX 千萬不要加這個，加了連 tab bar 都會變亂碼 XD。至於 linux 的話，我沒試過 XD。

## PlainTasks

PlainTasks 改了一些設定，可以先按 Preference -> Package Settings -> PlainTasks -> Settings User (在 Windows 上會稍微不同) 之後貼上下面內容。

```python
{
  "color_scheme": "Packages/Tomorrow Color Schemes/Tomorrow-Night-Bright.tmTheme",
  "font_size": 20,
  "font_face": "Source Code Pro",
  "line_numbers": true,
  "tab_size": 4,
  "fold_buttons": true,
  "spell_check": true,
  "dictionary": "Packages/Language - English/en_US.dic"
}
```
 
## murmur

雖然覺得在 Windows 上用 Sublime Text 已經很順了，但是不得不說在 Mac OSX 上的感覺更勝一籌啊 ... Orz。不過都回到 Mac OSX 上了，還是用 Vim 就好，unite.vim 真的很好很強大，有點愛不釋手 XD。