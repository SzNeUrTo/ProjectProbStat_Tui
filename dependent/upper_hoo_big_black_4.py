import random
from normalCards import deck

HOO_BIG_RED = ['1_king_red','2_airplane_red','3_eleplant_red']
HOO_BIG_BLACK = ['1_king_black','2_airplane_black','3_eleplant_black']

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
    while checkCase(cards[0:4]) :
        random.shuffle(cards)

    temp = [x for x in removeList]
    random.shuffle(temp)
    temp = removeList + temp
    inHand = temp[:4]+ cards[:4]
    outHand = cards[4:] + temp[4:]
    random.shuffle(outHand)

    cards = inHand + outHand
    return cards

def checkCase(cards):
    case1 = checkCase1(cards)
    case2 = checkCase2(cards)
    case3 = checkCase3(cards)
    return case1 or (case2 and case3) 

def checkCase1(cards):
    if '1_king_red' in cards :
        if '1_king_black' in cards :
            return True

def checkCase2(cards):
    if len(set(cards).intersection(HOO_BIG_RED)) == 2 :
        return True

def checkCase3(cards):
    if len(set(cards).intersection(HOO_BIG_BLACK)) == 2 :
        return True
    
def createPlayersHand(players, cards):
    for i in [0,8,16,24]:
        players.append(cards[i:i+8])
    return players

def cardsCheckUpper(players):
    for player in players:
        if players.index(player) != 0 :

            if player.count('1_king_red') == 1 :
                if player.count('2_airplane_red') >= 2 :
                    if player.count('3_eleplant_red') >= 1 :
                        return 1

            if player.count('1_king_black') == 1 :
                if player.count('2_airplane_black') >= 1 :
                    if player.count('3_eleplant_black') >= 2 :
                        return 1
    return 0

samapleSpace = 100000.0
event = 0.0
for round in range(1, int(samapleSpace+1)):
    hoo_little_red= ['4_boat_red', '5_horse_red', '6_biggun_red']
    players = []
    cards = deck()
    cards = randomCards(cards, hoo_little_red)
    players = createPlayersHand(players, cards)
    event += cardsCheckUpper(players)
    printCardsPlayers(players)
    players = []

print '=' * 150
print 'event ' + str(event)
print 'samapleSpace ' + str(samapleSpace)
print str(event / samapleSpace * 100) + ' %'
