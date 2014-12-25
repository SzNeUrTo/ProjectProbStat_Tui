import random
form = ['1_king'] + [ '2_airplane', '3_eleplant', '4_boat', '5_horse', '6_biggun'] * 2 + ['7_soldier'] * 5
cards = [x+y for y in ['_red', '_black'] for x in form]

n = 1000000.0
sum = 0
for round in range(1, int(n+1)):
    random.shuffle(cards)
    players = []
    for i in [0,8,16,24]:
        players.append(cards[i:i+8])
    #print '=================================================================================================='
    player_card = ''
    for i in range(0,4):
        players[i].sort()
        if players[i].count('7_soldier_red') == 4:
            sum += 1
        player_card = ' '.join(players[i])
print sum
percent = sum / n * 100
print str(percent) + ' %'
percent /= 4.0
print str(percent) + ' %'
