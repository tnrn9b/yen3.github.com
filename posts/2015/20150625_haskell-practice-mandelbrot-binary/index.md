<!--
.. link: 
.. description: 
.. tags: all, haskell, practice
.. date: 2015/06/25 23:41:26
.. title: [Haskell Practice] Mandelbrot set
.. slug: 20150625_haskell-practice-mandelbrot-binary
-->

老實說，原本以為會寫很一篇比較長的 blog post ，但是想想之後，做的都是簡單的事情，所以就簡單記錄一下。

測試的編譯指令是 `ghc -O2 Mandelbrot.hs -rtsopts -threaded -fllvm`

程式碼如下。基本上 Mandelbrot.hs 可以利用 `./Mandelbrot par 100 +RTS -N2 -s` 產生資料，該 output data 的前半部是 x points，後半部是 y points。再利用 `python plotMandelbrot.py` 把圖畫出來。

在 2010 late MBP15 (Intel Core i5 2.4 Ghz, 8Gb) 上跑 `./Mandelbrot par 100 +RTS -N2 -s` (2 threads) 約 25 secs 左右，單核心約 45 secs 左右，這速度是不快，不過暫時應該不會再改了，因為還有其他的資料想看 ... ([熱帶魚](http://chimera.labs.oreilly.com/books/1230000000929) 在 Chapter 6 也實作 Mandelbrot，使用 GPU 加速，只花了 10 secs，而且精細的多)。 

<script src="https://gist.github.com/yen3/8bc2f108cb8b6739edd7.js"></script>

最底下附上第一版程式，相較於最後一版其實做了不少修改如上。

1. 一開始使用 `Complex Double` 做計算，後來改用 `(Double,Double)`
2. 原生的 List 在 2 threads 以上的 GC 時間會特長 (沒有特地去找原因)，改用 `Data.Vector` 實作。
3. 一開始就產生全部的點去做運算耗費太多的時間，改傳點的平面範圍要算的時候再產生點。
4. 善用 [Bang patterns](https://downloads.haskell.org/~ghc/7.4.1/docs/html/users_guide/bang-patterns.html) 限制一些參數為 strict

```haskell
import Data.Complex
import Data.Binary.Put
import Data.Binary.IEEE754 (putFloat64le)
import qualified Data.ByteString.Lazy as BL
 
maxIteration :: Integer 
maxIteration = 3000 
 
pointSize :: Integer
pointSize = 2000 
 
isMandelPoint :: Complex Double -> Bool
isMandelPoint p = q maxIteration p
    where q :: Integer -> Complex Double -> Bool
          q 0 _ = True 
          q t z = if r > 2 then False else q (t - 1) z'
              where z' = p + z^2
                    r = realToFrac . realPart . abs $ z' 
 
pointList :: (Double, Double) -> (Double, Double) -> [(Double, Double)]
pointList (xBegin, xEnd) (yBegin, yEnd) =
    [(x, y) | x <- axis xBegin xEnd, y <- axis yBegin yEnd] 
    where axis b e = takeWhile (<e) $ zipWith (+) (repeat b) (scanl1 (+) $ repeat dist)
              where dist = (e - b) / fromIntegral pointSize
 
mandelPointList :: [(Double, Double)] -> [(Double, Double)]
mandelPointList = filter (\(x, y) -> isMandelPoint $ x :+ y)
 
serDoublesData :: [(Double, Double)] -> Put
serDoublesData zs = mapM_ putFloat64le $ xs ++ ys 
                    where (xs, ys) =  unzip zs
                                
main :: IO ()
main = do let fn = "mandelbot.bin" 
          let p = mandelPointList $ pointList (-2, 1) (0, 1)
          BL.writeFile fn (runPut (serDoublesData p))
          putStrLn $ "Finish write " ++ fn
```

練習寫這個程式算是長知識，因為很多基本的事其實都不太會，做個記錄哩。