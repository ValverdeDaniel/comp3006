
###Background Information
#The counting system works by keeping a running total in your head (hot Count) that tracks the ratio between high and low cards.
# the counting system will have a positive running caount when the deck has more high cards than low cards.
# a deck that has more high cards than low cards is called a hot deck and offers the player advantages.
# first the player is more likely to get black jack or atleast be dealt a higher starting hand. second the dealer is more likely to bust
# In this game you are not playing Black Jack but just training for the scenario that you are playing Black Jack and want to count cards.

###RULES OF GAME
#In this game we use the hi-lo strategy
#Each card is assigned a +1, -1, or 0 value which you add to your running count which we call the hot Count:
#Cards between 2-6 are +1
#Cards between 7-9 are 0
#Cards between 10-Ace are -1
#for example at the beginning of the game your hot Count will start at 0 but as soon as you draw one card lets say a King
## then  your hot Count will be -1 ; lets say you draw a Queen next your hot Count will be -2 you keep going until you run out of cards or mess up

# alias for shuffle as shuffle
from random import shuffle as shuffle
#alias for copy as copy
import copy as copy

print('Welcome To the Card Counting Trainer, \n The idea is to simulate holding a deck of cards and trying to ')
print('The rules of the game for cards with ranks are: ')
print(' from 2 - 6 the hot Count will increment by +1 \n from 7 - 9 the hot Count will not increment \n from 10 - Ace hot Count will increment by -1')
# Card Class
class Cards:
    def __init__(self):
        values = ['Ace of ', '2 of ', '3 of ', '4 of ', '5 of ', '6 of ', '7 of ', '8 of ', '9 of ', '10 of ', 'Jack of ', 'Queen of ', 'King of ']
        suites = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.deck = [j + i for j in values for i in suites]
        self.hotCount = 0

    def shuffle(self):
        shuffle(self.deck)

    def drawCard(self):
        self.hands = [self.deck.pop()]


#instantiating cards
c = Cards()
c.shuffle()

#defining which cards create +1 or -1
ups = ['2', '3', '4', '5', '6']
downs = ['10', 'Jack', 'Queen', 'King', 'Ace']

def game():
    if len(c.deck) > 0:
        c.drawCard()
        print('')
        print('The current card is: ', c.hands)
        #if the card is 10-A hotCount -1
        if any(x in str(c.hands) for x in downs):
#             print('the deck is getting colder')
            c.hotCount -= 1
        #if the card is 2-6 hotCount +1
        if any(y in str(c.hands) for y in ups):
#             print('the deck is getting hotter')
            c.hotCount += 1
        #we will tell you the answer for the first couple of cards so you learn how to play
        if len(c.deck) > 49:
            print('the current hot count is: ', c.hotCount)
        print('Type in a number for the exact Hot Count I hope you are keeping track')
        a = input()
        try:
            #put a shallow copy just for homeworks sake
            a = copy.copy(int(a))
            # if you set a = c.hotcount you can type any number and simulate what it feels like to win!
            # a = c.hotCount
            if a == c.hotCount:
                #recursively calling game to keep playing
                game()
            else:
                print('wrong count!')
                print('Ending Hot Count: ', c.hotCount)
        except:
            print('Ending Hot Count: ', c.hotCount)
            print('you chose poorly!')

game()

print('wow you made it', 52-len(c.deck), 'cards deep')
if len(c.deck) <= 0:
    print('You are really good at this you won!')
