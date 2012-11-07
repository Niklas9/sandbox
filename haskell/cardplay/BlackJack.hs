module BlackJack where
import Cards
import Wrapper

hand2 :: Hand
hand2 = Add (Card (Numeric 2) Hearts)
            (Add (Card Jack Spades) Empty)

-- Task 3.2:
-- size hand2
-- = size (Add (Card (Numeric 2) Hearts)
--             (Add (Card Jack Spades) Empty)
-- = 1 + size (Add (Card Numeric 2) Hearts)
-- = 1 + 1 + 0
-- = 2


hand3 :: Hand
hand3 = Add (Card Queen Spades) Empty

hand4 :: Hand
hand4 = Add (Card Queen Hearts)
--            (Add (Card King Hearts))
            (Add (Card (Numeric 2) Hearts) Empty)

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
numberOfAces h = 1

getCard :: Hand -> Card
getCard (Add card hand) = card

value :: Hand -> Integer
value h = 3

gameOver :: Hand -> Bool
gameOver h = (value h) >= 21

--winner :: Hand -> Hand -> Player
--winner h1 h2 | (value h1) == (valueh2) = 
--             | otherwise = (value h1) > (value h2)

