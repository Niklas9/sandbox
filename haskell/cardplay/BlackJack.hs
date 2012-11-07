module BlackJack where
import Cards
import Wrapper


-- Task 3.2:
-- size hand2
-- = size (Add (Card (Numeric 2) Hearts)
--             (Add (Card Jack Spades) Empty)
-- = 1 + size (Add (Card Numeric 2) Hearts)
-- = 1 + 1 + 0
-- = 2


-- Task 3.3:
empty :: Hand
empty = Empty

valueRank :: Rank -> Integer
valueRank Ace = 11
valueRank (Numeric n) = n
valueRank _ = 10

valueCard :: Card -> Integer
valueCard c = valueRank (rank c)

numberOfAces :: Hand -> Integer
numberOfAces Empty = 0
numberOfAces (Add c h)
        | (rank c) == Ace = 1 + numberOfAces h
        | otherwise = 0 + numberOfAces h

value :: Hand -> Integer
value Empty = 0
value (Add c h)
        | ((rank c) == Ace) && (numberOfAces h == 0) = valueCard c + 10 + (value h)
        | otherwise = (valueCard c) + (value h)

gameOver :: Hand -> Bool
gameOver h = (value h) > 21

winner :: Hand -> Hand -> Player
winner h1 h2
        | gameOver h1 = Bank
        | gameOver h2 = Guest
        | (value h1) <= (value h2) = Bank
        | (value h1) > (value h2) = Guest
