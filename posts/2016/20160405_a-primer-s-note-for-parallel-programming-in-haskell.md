<!--
.. link: 
.. description: 
.. tags: all, haskell, note
.. date: 2016/04/05 11:57:05
.. title: A primer's note for parallel programming in Haskell
.. slug: 20160405_a-primer-s-note-for-parallel-programming-in-haskell
-->

- Functional Thursday #33
- 2015.12.03
- Yen3 (yen3rc@gmail.com)

---

### About the slide 

- 這份投影片是 [Parallel and Concurrent Programming in Haskell](http://chimera.labs.oreilly.com/books/1230000000929) -
  Chatper 1 ~ 5 的筆記

- 主題包含 
    - Eval monad 
    - Par monad
    - Repa

- 今天的內容皆與 data-level parallelism 相關 
- 在 Haskell 中，一個較容易平行化 function 是 `map`，這份投影片會很常
  討論到它。

---

### Definition of Parallel 

- A __parallel__ program is one that uses a multiplicity of computational
  hardware (e.g., several processor cores) to perform a computation more
  quickly.
- Parallel programming in Haskell is deterministic: The parallel program always
  produces the same answer, regardless of how many processors are used to run
  it.

<!------->
<!--## Self-study -->
<!--- 在進入正題之前，先談幾個小筆記-->
<!--- Normal form, weak-head normal form and `force` function-->
<!--- unboxed type & boxed type-->
<!--- Bang patterns-->
<!--- Data.Vector package-->

---

### The status of value in ghc (1/)

- There are three conditions of a value.
    - Unevaluated 
    - Weak-Head Normal Form (WHNF) - evaluated with first constructor
    - Normal Form (NF) - fully evaluated

---

### The status of value in ghc (2/)

- `sprint` - prints a value without forcing its evaluation
- `seq`: only far as the first constructor and doesn't evaluate any more of
  the structure. It evaluates first argument to WHNF.
  
```haskell
seq :: a -> b -> b
```


---

### The status of value in ghc (3/)

- Example 

```haskell
Prelude> let x = 1 + 2 :: Int
Prelude> let y = x + 1
Prelude> :sprint x
x = _
Prelude> :sprint y
y = _
Prelude> seq y ()
()
Prelude> :sprint x
x = 3
Prelude> :sprint y
y = 4
```

---

### The status of value in ghc (4/)

```haskell
Prelude> let xs = map (+1) [1..10] :: [Int]
Prelude> :sprint xs
xs = _
Prelude> seq xs ()
()
Prelude> :sprint xs
xs = _ : _
Prelude> length xs
10
Prelude> :sprint xs
xs = [_,_,_,_,_,_,_,_,_,_]
Prelude> sum xs
65
Prelude> :sprint xs
xs = [2,3,4,5,6,7,8,9,10,11]
```

---

### `force` function 

- `force` - fully evaluated it's argument and returns it. (WHNF into NF)

```haskell
import Control.DeepSeq

class NFData a where
    rnf :: a -> ()      -- reduce to normal-form
    rnf a = a `seq` ()

deepseq :: NFData a => a -> b -> b
deepseq a b = rnf a `seq` b 

force :: NFData a => a -> a   
force x = x `deepseq` x
```

- `seq`: only far as the first constructor and doesn't evaluate any more of
  the structure. It evaluates first argument to WHNF.
  
<!-- deepseq: fully evaluates its argument and then returns () -->


---

### Eval monad 

- Decoupling of the algorithm from the parallelism
- The type declaration for eval monad 

```haskell
data Eval a
instance Monad Eval

runEval :: Eval a -> a
rpar :: a -> Eval a   -- rpar :: Strategy a 
rseq :: a -> Eval a   -- rseq :: Strategy a
```

- `rpar` - evaluate its argument in parallel.
- `rseq` - Evaluate the argument and wait for the result.
    - evaluates its argument to WHNF.

<!--
- The argument of `rpar` is also named **spark**.
-->


---

### Eval monad - simple example

- Example

```haskell
runEval $ do
    a <- rpar (f x)
    b <- rseq (f y)
    rseq a
    return (a, b)
```

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/24606632@N05/26219016196/in/dateposted-public/" title="eval_monad_simple_example"><img src="https://farm2.staticflickr.com/1717/26219016196_6d47d9e102.jpg" width="800" height="328" alt="eval_monad_simple_example"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

---

### Eval monad - Strategy 

- Strategy - modularize parllel code by separating the algorithm from the
  parallelism 
    - use `using` function to add parallelism with the existing codes
    - `withStrategy`- a another version of `using` with the arguments flipped

```haskell 
type Strategy a = a -> Eval a

using :: a -> Strategy a -> a
x `using` s = runEval (s x)

withStrategy :: Strategy a -> a -> a
withStrategy s x = runEval (s x)
```

---

### Eval monad - Strategy 

- The `rpar`, `rseq` are also Strategies.

```haskell
rpar :: Strategy a
rseq :: Strategy a
```

- You could write the algorithm first and add the parallelism code later
  ideally.

---

### Eval monad - example for pair 

- Example

```haskell
import Control.Parallel.Strategies
import Control.DeepSeq

evalPair :: Strategy a -> Strategy b -> Strategy (a,b)
evalPair sa sb (a,b) = do
    a' <- sa a
    b' <- sb b
    return (a',b')
```

---

### Eval monad - example for pair


```haskell
rparWith :: Strategy a -> Strategy a
rparWith s a =
    do
        ra <- rpar a
        sa <- s ra
        return sa 

(+) 1 2             -- (1-1)  
((+) 1 2, (+) 3 4)  -- (1-2)

(+) 1 2 `using` rpar   -- (2-1)
<!--((+) 1 2, (+) 3 4) `using` evalPair (rparWith rseq) (rparWith rseq)  -- (2-2)-->
((+) 1 2, (+) 3 4) `using` evalPair (rparWith rseq) (rparWith rseq)  -- (2-2)
```

- (1-1), (1-2) - sequential version
- (2-1), (2-2) - parallel version and reduce the value to WHNF

<!-- 
```haskell
(+) 1 2 `using` rpar (rseq . force) -- (3-1)
((+) 1 2, (+) 3 4) `using` evalPair (rpar . rseq . force) (rpar . rseq . force) -- (3-2)
((+) 1 2, (+) 3 4) `using` evalTuple2 ((rpar >> rseq) . force) ((rpar >> rseq) . force)
```

- (3-1), (3-2) - parallel version and reduce the value to NF 
- `parTuple2` and `evalPair` functions are the same
-->

---

### Eval monad - some help functions (1/)

- About some helper function
    - `rdeepseq` - evaluates the argument to NF 
```haskell
rdeepseq :: NFData a => Strategy a
rdeepseq x = rseq (force x)
```
    - `rparWith` - wraps the Strategy s in an `rpar`
```haskell
rparWith :: Strategy a -> Strategy a 
```

---

### Eval monad - some help functions (2/)

- The code reduced to NF in previous slide could also be written as 

```haskell
-- NF 
(+) 1 2 `using` rparWith rdeepseq 
((+) 1 2, (+) 3 4) `using`
    evalPair (rparWith rdeepseq) (rparWith rdeepseq)
```

---

### Eval monad - parallelize `map` 

```haskell
parMap :: (a -> b) -> [a] -> [b]
parMap f xs = map f x `using` parList rseq 

evalList :: Strategy a -> Strategy [a]
evalList start [] = return []
evalList start (x:xs) = do
    x' <- start x
    xs' <- evalList start xs
    return (x': xs')

parList :: Strategy a -> Strategy [a]
parList start = evalList (rparWith start)
```

- `parMap` will calculate its list to WHNF
- `parList` - evaluate the list element in parallel 

---

### Eval monad 

- Example

```haskell
import Control.Parallel.Strategies
import Control.DeepSeq

map (+1) [1..100]  -- (1) 
map (+1) [1..100] `using` parList rseq -- (2)
map (+1) [1..100] `using` parList rdeepseq  -- (3)
```

- (1) sequential version
- (2) parallelize version reduce value to WHNF
- (3) parallelize version reduce value to NF 

---

### Example - Mandelbrot set

- You could get more details
  from [my blog post](https://yen3.github.io/posts/2015/20150625_haskell-practice-mandelbrot-binary/).

- some type define

```haskell
type Point = (Double, Double)
type Range = (Double, Double)
type Plane = (Range, Range)
```

- sequential version

```haskell
planePoints :: Plane -> V.Vector Point

mandelSet :: Plane -> V.Vector Point
mandelSet = planeToMandelPoints
```

---

### Example - Mandelbrot set


- basic parallel version with `parList`

```haskell
splitPlane :: Integer -> Plane -> [Plane]

mandelSetStart :: Integer -> Plane -> V.Vector Point
mandelSetStart size p = V.concat
    (map planeToMandelPoints (splitPlane size p)
     `using` parList rseq)
```

- In  2010 late MBP15 (Intel Core i5 2.4 Ghz, 8Gb)
    - sequential - about 45 secs
    - run in 2 cores - about 25 secs (`./Mandelbrot par 100 +RTS -N2 -s`)


---

### Par Monad 

- __Goal__
    - be more explicit about granularity and data dependences 
    - Avoid the reliance on lazy evaluation, but without sacrificing the
      determinism that we value for parallel programming.
    - The parallel computations are pure (and deterministic)
- The library is implemented entirely as a Haskell library
    - You can accommodate alternative scheduling strategies.

---

### Par Monad 

- Par monad - a monad for parallel computation 
  
```haskell
newtype Par a

instance Applicative Par
instance Monad Par

runPar :: Par a -> a    -- produce a pure result.
fork :: Par () -> Par () -- the way to create parallel tasks
```

- IVar - results are communicated through IVars

```haskell
data IVar a 

new :: Par (IVar a)
put :: NFData a => IVar a -> a -> Par ()
get :: IVar a -> Par a
```

---

### Par Monad 

- IVar

```haskell
data IVar a 

new :: Par (IVar a)
put :: NFData a => IVar a -> a -> Par ()
get :: IVar a -> Par a
```

- `IVar` -- as a box that stars empty
- `put` -- store a value in the box 
    - All values communicated through IVars are fully evaluated. There is a head-strict version `put_` 
- `get` -- read the value. If the box is empty, it waits until the box is filled
  by put. The `get` operation does not remove the value from the box. Once the
  box is full. It stays the state constantly.

---

### Par Monad 

- Example 

```haskell
runPar $ do
    i <- new
    j <- new
    fork (put i (fib n))
    fork (put j (fib m))
    a <- get i
    b <- get j
    return (a+b)
```

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/24606632@N05/25642271873/in/dateposted-public/" title="par_monad"><img src="https://farm2.staticflickr.com/1609/25642271873_74a6b5c51e_c.jpg" width="800" height="230" alt="par_monad"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

---

### Par Monad 

- `spawn` - Like fork, but returns a IVar that can be used to query the result
    of the forked computation. Therefore spawn provides __futures__ or
    __promises__.
- `parMap` - parallel version map implemented with par monad

<!-- Yen3: need to review how to use `spawn` individually.  -->

```haskell
spawn :: NFData a => Par a -> Par (IVar a)
spawn p = do
    i <- new
    fork (do x <- p; put i x)
    return i

parMap :: NFData b => (a -> b) -> [a] -> Par [b]
parMap f as = do
    ibs <- mapM (spawn . return . f) as
    mapM get ibs
```

<!--
f :: a -> b
return . f :: a -> m b
spawn . return . f :: a -> Par (IVar a)
-->

---

### Example - prime number 

- Example
    - `primeIntVector` - Eval monad 
    - `primeIntVector'` - Par monad 


```haskell
primeIntVector :: Int -> VU.Vector Int
primeIntVector n =
    let
        ls = genNumberRange 0 n 100
    in
        VU.concat (map (uncurry primes) ls `using` parList rseq)


primeIntVector' :: Int -> VU.Vector Int
primeIntVector' n =
    let
        ls = genNumberRange 0 n 100
    in
        VU.concat $ Par.runPar $ Par.parMap (uncurry primes) ls
```

---

### Difference between `Par` and `Eval` 

- Par Monad 
    1. Always evaluate its value to normal form. It avoids the problem
       about the weak-normal form
    2. The cost of calling `runPar` function is bigger then `runEval` 
    3. Easy to redefine the scheduling strategy

---

### Difference between `Par` and `Eval`

- Eval Monad
    1. Need use `force` function to evaluate its value from weak-head normal
       form to normal form. It’s suitable for lazy data structure
    2. The cost of calling `runEval` function is free
    3. Provide the speculative parallelism 
    4. Eval Monad has more diagnostics in ThreadScope compared Par Monad.

- [Reference](https://stackoverflow.com/questions/23326920/difference-between-par-monad-and-eval-monad-with-deepseq)

<!--- What’s the pitfall of Eval Monad ? -->
<!--- What’s the pitfall of Par Monad ?-->

---

### Repa

- Repa - REgular PArallel arrays
- **Goal**
    - efficient numerical array computations in Haskell and run them in
      parallel 
- It could provides efficient unboxed data computation, but not Par monad and
  Strategy monad   
    - Repa also support boxed data.

---

### Repa - type

- The array type

```haskell
data Array r sh e
```

- `r` -  representation type 
- `e` - element type 
- `sh` - the shape of array (the dimension(s) of array)

```haskell
data Z = Z    -- scalar data
data tail :. head = tail :. head

type DIM0 = Z
type DIM1 = DIM0 :. Int
type DIM2 = DIM1 :. Int
```

---

### Repa - array

- how to create an array with `Array` type ?
    - `fromListUnboxed` - from list of unboxed type
    - `fromUnboxed` - from the vector with `Data.Vector.Unboxed` type
    - `fromFunction` - from the shape information to generate the array
    - ... etc

```haskell
fromListUnboxed :: (Shape sh, Unbox a) => sh -> [a] -> Array U sh a
fromFunction :: sh -> (sh -> a) -> Array D sh a
fromUnboxed :: (Shape sh, Data.Vector.Unboxed e) :: sh -> e -> Array U sh e
```

<!-- 
the major difference between `fromListUnboxed` and `fromUnboxed`
   - `fromListUnboxed` - O(n). Convert a list to an unboxed vector array.
   - `fromUnboxed` - O(1). Wrap an unboxed vector as an array. 
-->

---

### Repa - create array example


- Example - create an array

```haskell
Prelude> import Data.Array.Repa as R
Prelude R> let a = R.fromListUnboxed (Z :. 10) [1..10] :: Array U DIM1 Int
Prelude R> :t a 
a :: Array U DIM1 Int

Prelude R> let b =  R.fromFunction (Z :. 10) (\(Z :. i) -> i + 1 :: Int)
Prelude R> :t b
b :: Array D (Z :. Int) Int

Prelude R > import qualified Data.Vector.Unboxed as VU
Prelude R VU> let v = VU.enumFromN 1 10 :: VU.Vector Int
Prelude R VU> let c = R.fromUnboxed (Z :. (VU.length v)) v
Prelude R VU> :t c
c :: Array U (Z :. Int) Int
```

---

### Repa - array computation 

- All array will transfer to a delayed array type (ex: `Array D sh e`)
  after array computations (ex: `Repa.map`)

```haskell
Repa.map :: (Shape sh, Source r a) =>
     (a -> b) -> Array r sh a -> Array D sh b

(+^) :: (Num c, Shape sh, Source r1 c, Source r2 c) =>
     Array r1 sh c -> Array r2 sh c -> Array D sh c
```

---

### Repa - compute

- `computeS` - calculate the array operations in sequentially.
- `computeP` - the same as `computeS` but in parallel.
    - the purpose of the monad is only to ensure that `computeP` operations are
      performed in sequence and not nested.
        - the simplest way to reduce the monad effect -- `runIdentity`
        - See page p.94 to get more information

```haskell
computeS :: (Load r1 sh e, Target r2 e) => Array r1 sh e -> Array r2 sh e
computeP :: (Monad m, Source r2 e, Target r2 e, Load r1 sh e) =>
    Array r1 sh e -> m (Array r2 sh e)
```

---

### Repa - array computation example

- calculate $e^x = \sum^{\infty}_{n=0}\frac{x^n}{n!} \forall x$

```haskell
import Data.Array.Repa as R
import Control.Monad.Identity

fact x = foldr (*) 1 [1..x]

enumN :: Int -> Array D DIM1 Double
enumN n = R.fromFunction (Z :. n) (\(Z :. i) -> fromIntegral i)  

exp' :: Int -> Double
exp' x = let
             ns = enumN 100
             ys = R.map (\n -> (((fromIntegral x)**n) / (fact n)))
                  ns 
         in
             runIdentity . R.sumAllP $ ys

```

<!--
```haskell
*Main R>  mapM_ print $ Prelude.zipWith (\x y -> abs (x-y)) (Prelude.map exp' [1..10]) (Prelude.map exp [1..10] :: [Double])
4.440892098500626e-16
1.7763568394002505e-15
7.105427357601002e-15
2.842170943040401e-14
2.842170943040401e-14
0.0
6.821210263296962e-13
4.547473508864641e-13
0.0
7.275957614183426e-12
```
-->



---

### Repa - example

- Example - prime numbers

```haskell
primeArray :: Int -> VU.Vector Int
primeArray n = let
                   a = genArray n
                   ps = runIdentity . Repa.computeUnboxedP . primeArrayCheck $
                        a :: Array U DIM1 Int
               in
                   VU.filter (/=0) (Repa.toUnboxed ps)
```

---

### Conclusion

- The simplest parallel method - parallel map
    - use `parMap` or `parList`

- Repa is useful especially for numeric calculation.

- The remaining part of [the book](http://chimera.labs.oreilly.com/books/1230000000929)
  is about.
    - Parallel programming with GPU ([`Data.Accelerate`](https://hackage.haskell.org/package/accelerate))
    - Concurrent programming



- Bool unbxoed type ?

