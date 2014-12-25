import random
from normalCards import deck

def printCardsPlayers(players):
    print '=' * 150
    for playerCards in players :
        playerCards.sort()
        cardString = ''
        for card in playerCards :
            cardString += card + ' '
        print 'player' + str(players.index(playerCards)+1) + ' ---> ' + cardString

def removeCards(cards, removeList):
    for item in removeList :
        while cards.count(item) != 0:
            cards.remove(item)
    return cards

def randomCards(cards, removeList):
    cards = removeCards(cards, removeList)
    random.shuffle(cards)
    while True :
        if cards[:3].count('7_soldier_red') <= 2 :
            break
        random.shuffle(cards)

    temp = removeList * 3
    inHand = temp + cards[:5]
    outHand = cards[5:] + removeList * 2
    random.shuffle(outHand)

    cards = inHand + outHand
    return cards

def createPlayersHand(players, cards):
    for i in [0,8,16,24]:
        players.append(cards[i:i+8])
    return players

def cardsCheckUpper(players):
    for player in players:
        if players.index(player) != 0 :
            if player.count('7_soldier_red') >= 3 :
                return 1
    return 0

samapleSpace = 100000.0
event = 0.0
for round in range(1, int(samapleSpace+1)):
    players = []
    cards = deck()
    cards = randomCards(cards, ['7_soldier_black'])
    players = createPlayersHand(players, cards)
    event += cardsCheckUpper(players)
    printCardsPlayers(players)
    players = []

print '=' * 150
print 'event ' + str(event)
print 'samapleSpace ' + str(samapleSpace)
print str(event / samapleSpace * 100) + ' %'
