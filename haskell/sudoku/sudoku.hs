module Sudoku where

import Data.Char
import Data.List
import Data.Maybe
import Test.QuickCheck

-------------------------------------------------------------------------------

example :: Sudoku
example =
    Sudoku
      [ [Just 3, Just 6, Nothing,Nothing,Just 7, Just 1, Just 2, Nothing,Nothing]
      , [Nothing,Just 5, Nothing,Nothing,Nothing,Nothing,Just 1, Just 8, Nothing]
      , [Nothing,Nothing,Just 9, Just 2, Nothing,Just 4, Just 7, Nothing,Nothing]
      , [Nothing,Nothing,Nothing,Nothing,Just 1, Just 3, Nothing,Just 2, Just 8]
      , [Just 4, Nothing,Nothing,Just 5, Nothing,Just 2, Nothing,Nothing,Just 9]
      , [Just 2, Just 7, Nothing,Just 4, Just 6, Nothing,Nothing,Nothing,Nothing]
      , [Nothing,Nothing,Just 5, Just 3, Nothing,Just 8, Just 9, Nothing,Nothing]
      , [Nothing,Just 8, Just 3, Nothing,Nothing,Nothing,Nothing,Just 6, Nothing]
      , [Nothing,Nothing,Just 7, Just 6, Just 9, Nothing,Nothing,Just 4, Just 3]
      ]

-------------------------------------------------------------------------------

type Block = [Maybe Int]
data Sudoku = Sudoku { rows :: [Block] }
    deriving (Show, Eq)


-- allBlankSudoku is a sudoku with just blanks
allBlankSudoku :: Sudoku
allBlankSudoku = Sudoku (replicate 9 (replicate 9 Nothing))

checkRowLengths :: [Block] -> Bool
checkRowLengths [] = True
checkRowLengths (x:xs)
    | length x == 9 = checkRowLengths xs
    | otherwise = False

-- isSudoku sud checks if sud is really a valid representation of a sudoku
-- puzzle
isSudoku :: Sudoku -> Bool
isSudoku s = checkRowLengths (rows s) == True

notNothing :: Maybe Int -> Bool
notNothing value = value /= Nothing

areRowsBlank :: [Block] -> Bool
areRowsBlank [] = True
areRowsBlank (x:xs)
    | all notNothing x == True = areRowsBlank xs
    | otherwise = False

-- isSolved sud checks if sud is already solved, i.e. there are no blanks
isSolved :: Sudoku -> Bool
isSolved s = areRowsBlank (rows s) == True

-------------------------------------------------------------------------------

printElements :: Block -> String
printElements [] = "\n"
printElements (x:xs)
    | x == Nothing = "." ++ l
    | otherwise = show (fromJust x) ++ l
    where
        l = printElements xs

printRow :: [Block] -> String
printRow [] = ""
printRow (x:xs) = printElements x ++ printRow xs

-- printSudoku sud prints a representation of the sudoku sud on the screen
printSudoku :: Sudoku -> IO ()
printSudoku s = putStrLn (printRow (rows s))

buildSudokuEl :: String -> Block
buildSudokuEl "" = []
buildSudokuEl (x:xs)
    | x == '.' = [Nothing] ++ l
    | otherwise = [Just (ord x - 48)] ++ l
    where
        l = buildSudokuEl xs

buildSudokuRows :: [String] -> [Block]
buildSudokuRows [] = []
buildSudokuRows (x:xs) = [buildSudokuEl x] ++ buildSudokuRows xs

-- readSudoku file reads from the file, and either delivers it, or stops
-- if the file did not contain a sudoku
readSudoku :: FilePath -> IO Sudoku
readSudoku fp =
    do
        s <- readFile fp
        let y = Sudoku (buildSudokuRows (lines s))
        if (isSudoku y)
            then return y
            else error "Not a Sudoku!"

-------------------------------------------------------------------------------

-- cell generates an arbitrary cell in a Sudoku
cell :: Gen (Maybe Int)
cell = frequency [(90, return Nothing), (10,
    do r <- choose(1,9)
       return (Just r))]

-- an instance for generating Arbitrary Sudokus
instance Arbitrary Sudoku where
  arbitrary =
      do rows <- sequence [ sequence [ cell | j <- [1..9] ] | i <- [1..9] ]
         return (Sudoku rows)

-- propSudoku 
prop_Sudoku :: Sudoku -> Bool
prop_Sudoku s = isSudoku s


-------------------------------------------------------------------------------

isOkayBlock :: Block -> Bool
isOkayBlock b = length (nub x) == length x
    where x = filter (\y -> y /= Nothing) b

-- fix some copy-n-paste programming here
blockSplit :: Block -> [Block]
blockSplit b = [take 9 b, take 9 (drop 9 b), take 9 (drop 9 b)]

get3x3Block :: [Block] -> Int -> Block
get3x3Block [] col = []
get3x3Block (x:xs) col = (take 3 (drop col x)) ++ (get3x3Block xs col)

-- fix some copy-n-paste programming here
block3x3 :: [Block] -> [Block]
block3x3 b = (blockSplit (get3x3Block b 0)) ++ (blockSplit (get3x3Block b 3)) ++ (blockSplit (get3x3Block b 6))

blocks :: Sudoku -> [Block]
blocks s = rows s ++ transpose (rows s) ++ block3x3 (rows s)

checkBlocks :: [Block] -> Bool
checkBlocks [] = True
checkBlocks (x:xs) 
    | isOkayBlock x == True = checkBlocks xs
    | otherwise = False

isOkay :: Sudoku -> Bool
isOkay s = checkBlocks (blocks s)

-------------------------------------------------------------------------------
