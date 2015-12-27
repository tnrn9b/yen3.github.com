<!--
.. link: 
.. description: 
.. tags: all, haskell, practice
.. date: 2015/07/12 18:46:49
.. title: [Haskell Practice] Primes
.. slug: 20150712_haskell-practice-primes
-->

這個問題以前就寫過，只是剛好今天有機會重寫一下。

```haskell
module Prime where

sqrtInt :: Int -> Int
sqrtInt = ceiling . sqrt . fromIntegral

genInspectList :: Int -> [Int]
genInspectList n
    | n < 5 = []
    | otherwise = takeWhile (<=n) $ 5 : [6*x + y | x <- [1..], y <- [1, 5]]

prime :: Int -> [Int] -> Bool
prime x is = all (\y -> x `mod` y /= 0) (takeWhile (<= sqrtInt x) is)

primes :: Int -> [Int]
primes x
    | x < 2 = []
    | x < 3 = [2]
    | x < 5 = [2, 3]
    | otherwise = [2, 3] ++ filter (`prime` is) ps
        where is = primes (sqrtInt x)
              ps = genInspectList x
```

ghci 執行結果如下

```

*Prime> primes 100
[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

```
