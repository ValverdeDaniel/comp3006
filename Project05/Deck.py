
def main():
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    tempS = []
    tempR = []
    i = 0
    j = 0
    x = 0
    y = 0
    #creating a list of suits in format ['spades', 'spades', 'spades', .....] so that there's 13 of each suit in a row
    while j < len(suits):
        while i < len(ranks):
            tempS.append(suits[j])
            i = i + 1
        i = 0
        j = j+1

    #creating list of ranks in format ['ace', '2', '3', ... 'ace', '2', '3'] four times
    while x < len(suits):
        while y < len(ranks):
            tempR.append(ranks[y])
            y += 1
        y = 0
        x += 1

    deck = list(zip(tempR, tempS))

    print(deck)

main()





