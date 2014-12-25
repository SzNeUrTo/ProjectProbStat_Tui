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
    while checkCase(cards[0:5]) :
        random.shuffle(cards)

    inHand = removeList + cards[:5]
    outHand = cards[5:] + removeList
    random.shuffle(outHand)

    cards = inHand + outHand
    return cards

def checkCase(cards):
    case1 = checkCase1(cards)
    case2 = checkCase2(cards)
    case3 = checkCase3(cards)
    case4 = checkCase4(cards)
    case5 = checkCase5(cards)
    return (case1 and case2 and case5) or (case1 and case4 and case5) or (case2 and case3 and case5)

def checkCase1(cards):
    if '1_king_red' in cards :
        return True

def checkCase2(cards):
    if '1_king_black' in cards :
        return True

def checkCase3(cards):
    if cards.count('2_airplane_red') == 2 \
    or cards.count('3_eleplant_red') == 2 :
        return True

def checkCase4(cards):
    if cards.count('2_airplane_black') == 2 \
    or cards.count('3_eleplant_black') == 2 :
        return True

def checkCase5(cards):
    if cards.count('4_boat_red') == 2 \
    or cards.count('5_horse_red') == 2 \
    or cards.count('6_biggun_red') == 2 :
        return True
    

def createPlayersHand(players, cards):
    for i in [0,8,16,24]:
        players.append(cards[i:i+8])
    return players

def cardsCheckUpper(players):
    for player in players:
        if players.index(player) != 0 :
            if set(['1_king_red','2_airplane_red','3_eleplant_red']).issubset(player) :
                return 1
            if set(['1_king_black','2_airplane_black','3_eleplant_black']).issubset(player) :
                return 1
            if set(['4_boat_red','5_horse_red','6_biggun_red']).issubset(player) :
                return 1
    return 0

samapleSpace = 100000.0
event = 0.0
for round in range(1, int(samapleSpace+1)):
    hoo_little_red_3 = ['4_boat_black', '5_horse_black', '6_biggun_black']
    players = []
    cards = deck()
    cards = randomCards(cards, hoo_little_red_3)
    players = createPlayersHand(players, cards)
    event += cardsCheckUpper(players)
    printCardsPlayers(players)
    players = []

print '=' * 150
print 'event ' + str(event)
print 'samapleSpace ' + str(samapleSpace)
print str(event / samapleSpace * 100) + ' %'
