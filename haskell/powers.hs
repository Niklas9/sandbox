import Data.List

-- Given power function
power :: Integer -> Integer -> Integer
power n k | k < 0 = error "power: negative argument"
power n 0 = 1
power n k = n * power n (k-1)


-- Part 1
-- Answer: it takes k+1 computing steps, the extra step due to k=0 is counted
--         as one additional step.


-- Part 2
power1 :: Integer -> Integer -> Integer
power1 n k | k < 0 = error "power: negative argument"
           | otherwise = product (genericReplicate k n)


-- Part 3
power2 :: Integer -> Integer -> Integer
power2 n k | k < 0 = error "power negative argument"
           | k == 0 = 1
           | even k = power2 (n*n) (div k 2)
           | odd k = n * power2 n (k-1)


-- Part 4
-- B.
prop_powers :: Integer -> Integer -> Bool
prop_powers n k = power n k == power1 n k && power n k == power2 n k

-- A./C.
-- Choosing a few test cases to test first valid inputs and corner cases,
-- later invalid inputs (such as negative exponent k) 
tcs = [(2, 2), ((-3), 2), (1, 0), (3, 3), (3, 4), (3, 5), (3, 6)]
tc_test = all (uncurry prop_powers) tcs
tc_invalid = prop_powers 3 (-9)  -- should return exception/error

-- D.
-- quickCheck fails on prop_powers for negative exponents (as intended),
-- defining prop_powers' to make sure we only handle positive exponent (k)
prop_powers' :: Integer -> Integer -> Bool
prop_powers' n k = (prop_powers n (abs k))
