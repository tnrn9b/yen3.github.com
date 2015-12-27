<!--
.. link: 
.. description: 
.. tags: all, haskell, practice
.. date: 2015/06/24 10:56:14
.. title: [Haskell Practice] Execute shell command
.. slug: 20150624_haskell-practice-execute-shell-command
-->

算是今天做的小練習，為了要讓 `ghc` 有 `-fllvm` 選項，發現 ghc 支援的 llvm 版本為 3.3，所以自己寫了一個程式練習執行 shell command

```haskell
import System.Directory
import System.FilePath.Posix
import Data.String.Utils
import Control.Applicative
import System.Process

main :: IO ()
main = do f <- filter (endswith "-3.3") <$> getDirectoryContents "./"
          let ori_f = map ("../../Cellar/llvm33/3.3_1/bin/" </>) f
          let ln_f = map ((</>) "llvm33" . (\x -> take (length x - 4) x)) f
          mapM_ (\(n, n') -> readProcess "ln" ["-s", n, n'] "") (zip ori_f ln_f)
```

在執行完 `brew install homebrew/versions/llvm33` 且建立好 `/usr/local/bin/llvm33` 資料夾後在 `/usr/local/bin` 用 `runhaskell` 執行 就可以了。

只是單純留下來備忘，有些 function 也是臨時查的 XD。
