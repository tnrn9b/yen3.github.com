<!--
.. link: 
.. description: 
.. tags: all, software
.. date: 2013/09/14 22:36:15
.. title: Generate a default new post file in nikola
.. slug: 20130914_generate-a-default-new-post-file-in-nikola
-->

鑑於要產生新文章每次都要寫這些 tag 實在很煩，所以索性自己寫了一段 script 來做這些事。

<script src="https://gist.github.com/yen3/6562566.js"></script>

在 nikola 的目錄下執行

```bash
./new_post_nikola.py "Generate a default new post in nikola"
```

就會產生相對應的檔案 
`posts/20130914_generate-a-default-new-post-file-in-nikola.md`

雖然我最後想做的不是這個，不過先做這擋著用。