<!--
.. link: 
.. description: 
.. tags: all, murmur, haskell
.. date: 2015/10/06 22:10:48
.. title: murmur (9) - Just for fun - Add from 0 to n in parallel
.. slug: 20151006_murmur-9-just-for-fun-add-from-0-to-n-in-parallel
-->

I stuided the [repa](https://hackage.haskell.org/package/repa) package today. I discover it supports parallel computation for both boxed type and unboxed type rather then only for unboxed type. It reminds me that I have to read the manual carefully.

Repa supports doing sum computation in parallel (see `sumP` in [repa doc](https://hackage.haskell.org/package/repa-3.4.0.1/docs/Data-Array-Repa.html)). I just write a parallel sum function for fun.

```haskell
import Data.Array.Repa as Repa
import qualified Data.Vector.Unboxed as VU
import Control.Monad.Identity

sumR :: Int -> Double
sumR n = let
            xs = VU.enumFromN 0 n
        in
            runIdentity (Repa.sumAllP (Repa.fromUnboxed (Z :. VU.length xs) xs))
        
main = putStrLn $ show . sumR $ 100000000
```

 Tomorrow's goal: [Accelerate package](https://hackage.haskell.org/package/accelerate).
