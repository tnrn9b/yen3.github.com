<!--
.. link: 
.. description: 
.. tags: all, programming, haskell
.. date: 2013/09/08 16:15:14
.. title: Some examples for reading/ writing files in Haskell
.. slug: read_write_haskell_pbpaste_20130914
-->

先貼材料，之後補文。

## Read the clipboard's content in Mac OSX

```haskell
processPaste' :: (String -> String) -> IO ()
processPaste' pd = putStrLn . pd =<< readProcess "pbpaste" [] []
```

```bash
Prelude System.Process> putStrLn =<< readProcess "pbpaste" [] []
http://hackage.haskell.org/packages/archive/process/1.0.1.1/doc/html/System-Process.html
Prelude System.Process> import Data.Char
Prelude System.Process Data.Char> putStrLn . (map toUpper) =<< readProcess "pbpaste" [] []
HTTP://HACKAGE.HASKELL.ORG/PACKAGES/ARCHIVE/PROCESS/1.0.1.1/DOC/HTML/SYSTEM-PROCESS.HTML
```

---

```haskell
-- Read the contents of clipboard
-- Ref: http://stackoverflow.com/questions/1712347/closest-equivalent-to-subprocess-communicate-in-haskell

import System.Process

processData :: String -> String
processData = (id :: String -> String)

processPaste pd = do
    let cmd = "pbpaste"
        args = []
        instr = []
    (rc, out, err) <- readProcessWithExitCode cmd args instr
    putStrLn $ pd out

main = processPaste processData

-- Run in ghci
-- Prelude> :l read_pbpaste.hs
-- [1 of 1] Compiling Main             ( read_pbpaste.hs, interpreted )
-- Ok, modules loaded: Main.
-- *Main> import Data.Char
-- *Main Data.Char> processPaste Data.Char.to
-- Data.Char.toLower  Data.Char.toTitle  Data.Char.toUpper
-- *Main Data.Char> processPaste $ map Data.Char.toUpper
-- Loading package array-0.4.0.1 ... linking ... done.
-- Loading package deepseq-1.3.0.1 ... linking ... done.
-- Loading package filepath-1.3.0.1 ... linking ... done.
-- Loading package old-locale-1.0.0.5 ... linking ... done.
-- Loading package time-1.4.0.1 ... linking ... done.
-- Loading package bytestring-0.10.0.2 ... linking ... done.
-- Loading package unix-2.6.0.1 ... linking ... done.
-- Loading package directory-1.2.0.1 ... linking ... done.
-- Loading package process-1.1.0.2 ... linking ... done.
-- ING PACKAGE ARRAY-0.4.0.1 ... LINKING ... DONE.
-- LOADING PACKAGE DEEPSEQ-1.3.0.1 ... LINKING ... DONE.
-- LOADING PACKAGE FILEPATH-1.3.0.1 ... LINKING ... DONE.
-- LOADING PACKAGE OLD-LOCALE-1.0.0.5 ... LINKING ... DONE.
-- LOADING PACKAGE TIME-1.4.0.1 ... LINKING ... DONE.
-- LOADING PACKAGE BYTESTRING-0.10.0.2 ... LINKING ... DONE.
-- LOADING PACKAGE UNIX-2.6.0.1 ... LINKING ... DONE.
-- LOADING PACKAGE DIRECTORY-1.2.0.1 ... LINKING ... DONE.
-- LOADING PACKAGE PROCESS-1.1.0.2 ... LINKING ... DONE.
-- HTTPS://EN.WIKIPEDIA.ORG/WIKI/CONTINUATION-PASSING_STYLE


```

## Read/ Write files

出處: Real World Haskell: Chapter 7

```haskell
processData :: String -> String
processData = (id :: String -> String)

main = interact $ processData

--- Run in command line
-- > runghc process_data.hs < input.txt
-- hello, world!
```

```haskell
processData :: String -> String
processData = (id :: String -> String)

main = do
    inStr <- readFile "input.txt"
    putStrLn $ processData inStr
```

```haskell
import System.IO

processData :: String -> String
processData = (id :: String -> String) 


main = do
    inh <- openFile "input.txt" ReadMode
    outh <- openFile "output.txt" WriteMode
    inpStr <- hGetContents inh
    
    let result = processData inpStr
    
    hPutStr outh result
    hClose inh
    hClose outh
```

-----
出處: [Tutorials/Programming Haskell/Argument handling: 2.1 Getting in arguments](http://www.haskell.org/haskellwiki/Tutorials/Programming_Haskell/Argument_handling#Getting_in_arguments)

```haskell
import System.IO
import System.Environment
import System.Exit

main = getArgs >>= parse >>= putStr . processData

processData :: String -> String
processData = (id :: String -> String)

parse ["-h"] = usage   >> exit
parse []     = getContents
parse fs     = concat `fmap` mapM readFile fs

usage   = putStrLn "Usage: readData [-h] [file ..]"
exit    = exitWith ExitSuccess
die     = exitWith (ExitFailure 1)
```