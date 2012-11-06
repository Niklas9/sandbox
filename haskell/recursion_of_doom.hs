-- just reimplementing some internal Haskell functions..
-- why, you may wonder? to learn, mister/miss!

maximum' :: (Ord a) => [a] -> a  
maximum' [] = error "maximum of empty list"  
maximum' [x] = x  
maximum' (x:xs) = max x (maximum' xs)

replicate' :: Integer -> Integer -> [Integer]
replicate' n x | n == 0 = []
replicate' n x | otherwise = [x] ++ replicate' (n-1) x

replicate'' :: (Num i, Ord i) => i -> a -> [a]
replicate'' n x
    | n <= 0   = []
    | otherwise = x:replicate'' (n-1) x
