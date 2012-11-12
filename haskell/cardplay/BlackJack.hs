module BlackJack where
import Cards
import System.Random
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

(<+) :: Hand -> Hand -> Hand
(<+) Empty h2 = h2
(<+) (Add c1 h1) h2 = Add c1 (h1 <+ h2)

prop_onTopOf_assoc :: Hand -> Hand -> Hand -> Bool
prop_onTopOf_assoc p1 p2 p3 = p1 <+ (p2 <+ p3) == (p1 <+ p2) <+ p3

prop_size_onTopOf :: Hand -> Hand -> Bool
prop_size_onTopOf h1 h2 = ((value h1) + (value h2)) == value (h1 <+ h2)

allCardsByRank :: [Rank] -> Suit -> Hand
allCardsByRank [] s = Empty
allCardsByRank (x:xs) s = (Add (Card x s)) (allCardsByRank xs s)

allCardsBySuit :: Suit -> Hand
allCardsBySuit s = allCardsByRank [Numeric 2, Numeric 3, Numeric 4, Numeric 5, Numeric 6, Numeric 7, Numeric 8, Numeric 9, Numeric 10, Jack, Queen, King, Ace] s

fullDeck :: Hand
fullDeck = allCardsBySuit Hearts <+ allCardsBySuit Diamonds <+ allCardsBySuit Clubs <+ allCardsBySuit Spades

draw :: Hand -> Hand -> (Hand, Hand)  -- first arg is deck
draw Empty hand = error "draw: The deck is empty."
draw (Add deckHand deckRest) hand = (deckRest, Add deckHand hand)

drawSpecific :: Integer -> Hand -> (Hand, Hand)
drawSpecific i hand
    | i > size(hand) = error "drawSpecific: out of bounds"
    | i == 1 = (hand', hand'') 
    | otherwise = (fst a <+ hand'', snd a)
    where 
        (hand', hand'') = draw hand Empty
        a = drawSpecific (i-1) hand'

playBankHlp :: Hand -> Hand -> Hand
playBankHlp deck hand 
    | (value hand) >= 16 = hand
    | otherwise = playBankHlp deck' bankHand' 
    where
        (deck', bankHand') = (draw deck hand)

playBank :: Hand -> Hand  -- first arg is deck
playBank deck = playBankHlp deck Empty

shuffle :: StdGen -> Hand -> Hand
shuffle g deck 
    | size(deck) == 0 = Empty
    | otherwise = hand'' <+ (shuffle g' hand')
    where
        (i, g') = randomR (1, size(deck)) g
        (hand', hand'') = drawSpecific i deck

prop_shuffle_sameCards :: StdGen -> Card -> Hand -> Bool
prop_shuffle_sameCards g c h = c `belongsTo` h == c `belongsTo` shuffle g h

belongsTo :: Card -> Hand -> Bool
belongsTo c Empty = False
belongsTo c (Add c' h) = c == c' || c `belongsTo` h

prop_size_shuffle :: StdGen -> Hand -> Bool
prop_size_shuffle g h = size (shuffle g h) == size h


implementation = Interface
    {
    iEmpty = empty,
    iFullDeck = fullDeck,
    iValue = value,
    iGameOver = gameOver,
    iWinner = winner,
    iDraw = draw,
    iPlayBank = playBank,
    iShuffle = shuffle
    }

main :: IO()
main = runGame implementation 
