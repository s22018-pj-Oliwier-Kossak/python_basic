import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

allCards = []
player1 = []
player2 = []

for color in colors:
    for figure in figures:
        allCards.append("%s - %s" % (color, figure))
print(allCards)

random.shuffle(allCards)
print(allCards)

max = len(allCards)
min = 0
while min < max:
    if min % 2 == 0:
        player1.append(allCards[min])
    else:
        player2.append(allCards[min])
    min +=1

print(player1)
print(player2)
