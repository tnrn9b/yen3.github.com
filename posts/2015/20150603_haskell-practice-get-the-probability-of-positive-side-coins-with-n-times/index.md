<!--
.. link: 
.. description: 
.. tags: all, haskell, practice
.. date: 2015/06/03 08:01:28
.. title: [Haskell Practice] Get the postive-edge probability for throwing a coin with n times
.. slug: 20150603_haskell-practice-get-the-probability-of-positive-side-coins-with-n-times
-->

很久很久以前 Josh 有寫過 one-linear code，不過我現在只能用 `(>>=)` 硬拼成一行 ... 估計我這樣子是做弊的方式，哈。


```haskell
module R1000 where

import System.Random

divI :: Fractional a => Int -> Int -> a 
a `divI` b = fromIntegral a / fromIntegral b

prob :: Fractional a => Int -> Int -> a 
x `prob` y = x `divI` y * 100.0

trues :: Int -> IO Int
trues n = newStdGen >>= \gen -> return $ length . filter (==True) $ (take n $ randoms gen :: [Bool])

positive :: Fractional r => Int -> IO r
positive n = trues n >>= \x -> return $ x `prob` n

positive' :: Fractional r => Int -> IO r
positive' n = newStdGen >>= \gen -> return (length . filter (==True) $ (take n $ randoms gen :: [Bool])) >>= \x -> return $ x `prob` n

positive'' :: Fractional r => Int -> IO r
positive'' n = do gen <- newStdGen
                  let pos_sides = length . filter (==True) $ (take n $ randoms gen :: [Bool])
                  return $ pos_sides `prob` n
```

在 ghci 輸出範例結果如下

```haskell
*R1000> positive 1000
50.7
*R1000> positive 10000
50.09
*R1000> positive 100000
50.248000000000005
*R1000> positive 1000
49.2
*R1000>
```
