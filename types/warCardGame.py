import random
colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []
player1 = []
player2 = []
for color in colors:
    for figure in figures:
        aCard = figure.copy()
        aCard['Color'] = color
        allCards.append(aCard)

random.shuffle(allCards)


for i in range(len(allCards)):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print(player1)
print(player2)


round = 0
x = 1
y = 0
listXY = []
count = 0
for i in range(10):
    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1['Power'] > card2['Power']:
            round += 1
            player1.append(card2)
            player1.append(card1)
            print("round", round, "player1", card1['Power'], card2['Power'])
        elif card2['Power'] > card1['Power']:
            round += 1
            player2.append(card1)
            player2.append(card2)
            print("round", round, "player2", card2['Power'], card1['Power'])
        elif card1['Power'] == card2['Power']:
            round += 1
            print("round", round, "remis", card2['Power'], card1['Power'])
            player1.append(card1)
            player1.append(card2)

        if len(player2) < 1:
            print("player 1 win")
            listXY.append(x)
            count += 1
        elif len(player1) < 1:
            print("player 2 win")
            listXY.append(y)
            count += 1

print(listXY)
print(listXY.count(1))
print(listXY.count(0))



