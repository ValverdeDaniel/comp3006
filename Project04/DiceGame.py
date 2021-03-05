import random as rand
print('Welcome To the Game of War Dice')
print('The rules are simple you will roll some dice versus a computer and the highest roll Wins!')
print('-----------------------------------------------------------------')
print('\n')

#Initial Game Settings
print('how many sides should the dice have?')
diceSides = int(input())
print('how many dice would you like to play with?')
diceQuantity = int(input())
print('how much money would you like to retrieve from the ATM')
startingCash = int(input())

#Defining Dice Object
class Dice:
    #constructor
    def __init__(self):
        self.sides = diceSides
        self.result = 0
        self.face = 1

    # All Comparison magic methods (__eq__, __ne__, __lt__, __gt__, __le__, __ge__)

    def __eq__(self, other):
        if type(self) == type(other):
            return(self.face == other.face)

    def __lt__(self, other):
        if type(self) == type(other):
            return(self.face < other.face)

    def __gt__(self, other):
        if type(self) == type(other):
            return(self.face > other.face)

    def __ne__(self, other):
        if type(self) == type(other):
            return(self.face != other.face)

    def __le__(self, other):
        if type(self) == type(other):
            return(self.face <= other.face)

    def __ge__(self, other):
        if type(self) == type(other):
            return(self.face >= other.face)

    def roll_dice(self):
        self.face = rand.randint(1,self.sides)

    def __str__(self):
        self.roll_dice()
        s = str(self.face)
        return s


#placing dice objects into CupOfDice Object
#Defining CupOfDice
class CupOfDice:
    def __init__(self, diceQuantity):
        self.numDice = diceQuantity
        self.cup = []

    def myDiceCup(self):
        for i in range(diceQuantity):
            self.cup.append(Dice())

    def __str__(self):
        s = str(self.cup)
        return s

    def rollCup(self):
        for i in range(len(self.cup)):
            self.cup[i].roll_dice()
            print(self.cup[i])

    def __add__(self, other):
        if type(self) == type(other):
            return CupofDice(self.face + other.face)

    def __eq__(self, other):
        if type(self) == type(other):
            return(self.face == other.face)

    def __lt__(self, other):
        if type(self) == type(other):
            return(self.face < other.face)

    def __gt__(self, other):
        if type(self) == type(other):
            return(self.face > other.face)

    def __ne__(self, other):
        if type(self) == type(other):
            return(self.face != other.face)

    def __le__(self, other):
        if type(self) == type(other):
            return(self.face <= other.face)

    def __ge__(self, other):
        if type(self) == type(other):
            return(self.face >= other.face)


#Defining Cash Object
class Gambling:

    def __init__(self):
        self.cash = startingCash

g = Gambling()
cc = CupOfDice(diceQuantity)
cc.myDiceCup()

#Just S
# \ome comments for my cupOfDice
# print(cc)
# r = cc.rollCup()
# # print(dir(r))
# print([cc.cup[i] for i in range(diceSides)])

def main():
    #if I have cash I can play the game and place a bet
    if g.cash > 0:
        print('you have ', g.cash, 'dollars, what is your bet or 0 to walk away' )
        bet = int(input())

        if bet > g.cash:
            print('chill, bet what you have')
            main()

        elif bet == 0:
            print('you walked away with $', g.cash)
            return

        #This is where the logic of the game play is used
        else:
            #utilizing logic for cupOfDice
            if diceQuantity > 1:
                print('You rolled: ')
                d1 = cc.rollCup()
                sum1 = sum([cc.cup[i].face for i in range(diceQuantity)])
                print('computer rolled: ')
                d2 = cc.rollCup()
                sum2 = sum([cc.cup[i].face for i in range(diceQuantity)])

                if sum1 > sum2:
                    g.cash = g.cash + bet
                    print('You WON this round!')
                elif sum1 < sum2:
                    g.cash = g.cash - bet
                    print('you LOST this round')
                elif sum1 == sum2:
                    print('it seems that it was a tie')
                else:
                    print('Something peculiar may have happened')

                print('Now Your Total Monies are: $', g.cash)
                print('-----------------------------------------------------------------')
                main()

            #utilizing logic for single dice with magic methods
            elif diceQuantity <= 1:
                d1 = Dice()
                print('You rolled', d1.__str__())
                d2 = Dice()
                print('computer rolled', d2.__str__())
                if d1.__gt__(d2):
                    g.cash = g.cash + bet
                    print('You WON this round!')
                elif d1.__lt__(d2):
                    g.cash = g.cash - bet
                    print('you LOST this round')
                elif d1.__eq__(d2):
                    print('it seems that it was a tie')
                else:
                    print('Something peculiar may have happened')

                print('Now Your Total Monies are: $', g.cash)
                print('-----------------------------------------------------------------')
                main()
    else:
        print('you are out of money')

if __name__ == '__main__':
    main()
