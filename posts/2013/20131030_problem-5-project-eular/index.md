<!--
.. link: 
.. description: 
.. tags: all, haskell
.. date: 2013/10/30 20:17:17
.. title: Problem 5 - Project Eular
.. slug: 20131030_problem-5-project-eular
-->

這是在前幾天寫的，算是沒有想這麼多，只是單純想要用 haskell 解決一個小問題而己。寫程式的感覺出乎意外的好，或許不用考慮太多邊寫邊練習才有辦法寫出 haskell program 吧我想 XD。

```haskell
import qualified Data.Map as Map
 
-- The answer for Problem 5
smallestMultiple :: Integer -> Integer
smallestMultiple n = Map.foldWithKey (\k v sm-> sm * (power k v)) 1 (numFactorMapList n)
 
numFactorMapList :: Integer -> Map.Map Integer Integer
numFactorMapList n = foldr mergeMap (Map.fromList []) (map numFactorMap [2..n])
 
mergeMap :: Map.Map Integer Integer -> Map.Map Integer Integer -> Map.Map Integer Integer
mergeMap = Map.unionWithKey (\k v1 v2-> if v1 > v2 then v1 else v2)
 
numFactorMap :: Integer -> Map.Map Integer Integer
numFactorMap = flip get_num_factor_map $ (Map.fromList [])
 
 
get_num_factor_map :: Integer -> Map.Map Integer Integer -> Map.Map Integer Integer
get_num_factor_map 0 m = m
get_num_factor_map 1 m = m
get_num_factor_map n m =
    if Map.member factor m then
        get_num_factor_map next_n (updateValue m)
    else
        get_num_factor_map next_n (insertValue m)
    where next_n = quot n factor
          factor = getFirstFactor n
          insertValue m = Map.insert factor 1 m
          updateValue m = snd $ Map.updateLookupWithKey (\k v-> if k == factor then Just (v+1) else Nothing) factor m
 
getFirstFactor :: Integer -> Integer
getFirstFactor = flip get_first_factor $ 2
 
get_first_factor :: Integer -> Integer -> Integer
get_first_factor 0 _ = 0
get_first_factor 1 _ = 1
get_first_factor 2 _ = 2
get_first_factor n p = if n `mod` p == 0 then p else get_first_factor n (p+1)
 
power _ 0 = 1
power 0 _ = 0
power x n  = let sqr k = k * k
                 half_n = n `div` 2
                 sqrHalfPower = sqr ( power x half_n )
             in if even n then sqrHalfPower else x * sqrHalfPower
```