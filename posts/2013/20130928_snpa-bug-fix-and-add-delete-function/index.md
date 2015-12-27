<!--
.. link: 
.. description: 
.. tags: all, tweet, snpa
.. date: 2013/09/28 00:27:06
.. title: SNPA: bug fix and add delete function
.. slug: 20130928_snpa-bug-fix-and-add-delete-function
-->


## Bug fix

* Fix the `CR` in the end of line error in Windows
    * use `\n` with new line wherever Mac OSX, Linux or Windows

## New function

* How to generate filename:
    * If `slug` column is not empty, the filename is `slug.md` 
    * If `English title` column is not empty, the filename is `{timestamp}_{English-title}.md`
        * If your title is not written in English, recommend to write the column. 
        * For example, if you write **How are you today**, the filename is `20130928_how-are-you-today.md`
    * If `title` column is not empty, the rule is as the same as the `English title` rule.
* Add delete function (included delete check) can remove a post
* If you change your slug in the existed post, the post will change filename to the new slug.

## Murmur

其實下班之後還是在想辦法增加功能，雖然是很想用 jQuery 讓頁面少一點，不過我上次用是兩年前的事，所以還是暫緩好了。不過如果這次要用，可能直接用 DOM 來寫，因為我要寫的功能其實真的沒有這麼多 XD。