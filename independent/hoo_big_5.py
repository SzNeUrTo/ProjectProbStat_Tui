import random
form = ['1_king'] + [ '2_airplane', '3_eleplant', '4_boat', '5_horse', '6_biggun'] * 2 + ['7_soldier'] * 5
cards = [x+y for y in ['_red', '_black'] for x in form]

n = 100000.0
sum = 0
for round in range(1, int(n+1)):
    random.shuffle(cards)
    players = []
    for i in [0,8,16,24]:
        players.append(cards[i:i+8])

    for player in players :
        if player.count('1_king_red') == 1 :
            if player.count('2_airplane_red') == 2 and player.count('3_eleplant_red') == 2 :
                sum += 1
    
print sum
percent = sum / n * 100
print str(percent) + ' %'
percent /= 4.0
print str(percent) + ' %'
