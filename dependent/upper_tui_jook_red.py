import random
from normalCards import deck
def removeCards(cards, removeList, cardsUpper):
    for item in cardsUpper:
        while cards.count(item) != 0 :
            cards.remove(item)
    cards.remove(removeList[0])
    cards.remove(removeList[0])

    cards += cardsUpper * 2
    return cards

def randomCards(cards, removeList, cardsUpper):
    random.shuffle(cards)
    cards = removeList * 2 + cards
    while set(cardsUpper).issubset(cards[2:8]):
        removeCards(cards, removeList, cardsUpper)
        random.shuffle(cards)
        cards = removeList * 2 + cards
    return cards

def printCardsPlayers(players):
    print '=' * 150
    for playerCards in players :
        playerCards.sort()
        cardString = ''
        for card in playerCards :
            cardString += card + ' '
        print 'player' + str(players.index(playerCards)+1) + ' ---> ' + cardString

def createPlayersHand(players, cards):
    for i in [0,8,16,24]:
        players.append(cards[i:i+8])
    return players

def cardsCheckUpper(players, cardsUpper):
    for player in players :
        for cardUpper in cardsUpper :
            if player.count(cardUpper) == 2 and players.index(player) != 0 :
                return 1
    return 0


samapleSpace = 100000.0
event = 0.0
for round in range(1, int(samapleSpace+1)):
    cards = deck()
    players = []
    cardsUpper = ['2_airplane_red', '2_airplane_black', '3_eleplant_red','3_eleplant_black','4_boat_red','4_boat_black','5_horse_red','5_horse_black','6_biggun_red','6_biggun_black']
    removeList = ['7_soldier_red']
    cards = removeCards(cards, removeList, cardsUpper)
    cards = randomCards(cards, removeList, cardsUpper)
    players = createPlayersHand(players, cards)
    event += cardsCheckUpper(players, cardsUpper)
    printCardsPlayers(players)

print '=' * 150
print 'event ' + str(event)
print 'samapleSpace ' + str(samapleSpace)
print str(event / samapleSpace * 100) + ' %'
