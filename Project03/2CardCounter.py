from random import shuffle
import keyboard

class Cards:
    def __init__(self):
        values = ['Ace of ', '2 of ', '3 of ', '4 of ', '5 of ', '6 of ', '7 of ', '8 of ', '9 of ', '10 of ', 'Jack of ', 'Queen of ', 'King of ']
        suites = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.deck = [j + i for j in values for i in suites]

    def shuffle(self):
        shuffle(self.deck)

#     def deal(self, n_players):
#         self.hands = [self.deck[i::n_players] for i in range(0, n_players)]

    def drawCard(self):
        ups = ['2', '3', '4', '5', '6']
        downs = ['10', 'Jack', 'Queen', 'King', 'Ace']
        self.hotCount = 0
        self.hands = [self.deck.pop()]
        print('from withindrawcard',self.hands)
        if any(x in self.hands for x in downs):
            print('the deck is getting colder')
            self.hotCount -= 1
        if any(y in self.hands for y in ups):
            print('the deck is getting hotter')
            self.hotCount += 1
        print('from withindrawcard', self.hotCount)


c = Cards()
global hotCount
hotCount = 0
c.shuffle()
print(c.deck)
c.drawCard()



# print(c.deck)
# print(c.hands)
# c.drawCard()

# print('strhands', str(c.hands))
ups = ['2', '3', '4', '5', '6']
downs = ['10', 'Jack', 'Queen', 'King', 'Ace']

def game():
    c.drawCard()
    print(c.hands)
#     hotCount = 0
#     if any(x in str(c.hands) for x in downs):
#         print('the deck is getting colder')
#         hotCount -= 1
#         return hotCount
#     if any(y in str(c.hands) for y in ups):
#         print('the deck is getting hotter')
#         hotCount += 1
#         return hotCount

game()



# if 'Jack' or 'Queen' or 'King' or 'Ace' in str(c.hands):
#     print('the deck is getting colder')
#     hotCount -= 1
# if any(x in str(c.hands) for x in downs):
#     print('the deck is getting colder')
#     hotCount -= 1


# if any(y in str(c.hands) for y in ups):
#     print('the deck is getting hotter')
#     hotCount += 1
print('lastHotCount',hotCount)
print(len(c.deck))
