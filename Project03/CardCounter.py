import random

print("Welcome To Card Counter")

class Card(object):

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def show(self):
        print("{} of {}".format(self.rank, self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))


    def show(self):
#         deckCount = 0
        for c in self.cards:
            c.show()
#             deckCount+=1
#         print(deckCount)

    def count(self):
        deckCount = 0
        for c in self.cards:
            deckCount += 1
        print(deckCount)

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discards(self):
        return self.hand.pop()

#creating an instance of this card
# card = Card("Clubs", 6)
# card.show()

#Shuffling and showing Deck
deck = Deck()
deck.shuffle()
# deck.show()

#bob draws two cards and shows his hand
bob = Player("Bob")
print('bobs cards')
bob.draw(deck).draw(deck)
bob.showHand()
print('deckCount')
deck.count()

print('bobs cards')
bob.draw(deck).draw(deck)
bob.showHand()
print('deckCount')
deck.count()
# card = deck.draw()
# card.show()
