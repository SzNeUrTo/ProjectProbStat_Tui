import random
form = ['1_king'] + [ '2_airplane', '3_eleplant', '4_boat', '5_horse', '6_biggun'] * 2 + ['7_soldier'] * 5
cards = [x+y for y in ['_red', '_black'] for x in form]
for x in cards :
    print x

n = 1000000.0
for round in range(1, int(n+1)):
    random.shuffle(cards)
    players = []
    for i in [0,8,16,24]:
        players.append(cards[i:i+8])
    print '=================================================================================================='
    player_card = ''
    for i in range(0,4):
        players[i].sort()
        player_card = ' '.join(players[i])
        print 'round %02d ' % round + 'player' + str(i+1) + ' ' + player_card
