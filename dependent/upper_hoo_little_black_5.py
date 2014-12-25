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
        if len(set(['1_king_red','2_airplane_red','3_eleplant_red']).intersection(cards[:3])) == 0 \
        or len(set(['1_king_black','2_airplane_black','3_eleplant_black']).intersection(cards[:3])) == 0 \
        or len(set(['4_boat_red','5_horse_red','6_biggun_red']).intersection(cards[:3])) <= 1 :
            break
        random.shuffle(cards)

    temp = removeList * 2
    random.shuffle(temp)
    inHand = temp[:5]
    outHand = temp[5:]

    inHand = inHand + cards[:3]
    outHand = cards[3:] + outHand
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

            if player.count('1_king_red') == 1 :
                if player.count('2_airplane_red') == 2 :
                    if player.count('3_eleplant_red') == 2 :
                        return 1

            if player.count('1_king_black') == 1:
                if player.count('2_airplane_black') == 2 :
                    if player.count('3_eleplant_black') == 2 :
                        return 1

        count_boat_red = 0
        count_horse_red = 0
        count_biggun_red = 0
        count_boat_red = player.count('4_boat_red')
        count_horse_red = player.count('5_horse_red')
        count_biggun_red = player.count('6_biggun_red')
        sum_count_hoo_red_little = count_boat_red + count_horse_red + count_biggun_red
        if sum_count_hoo_red_little >= 5 :
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
