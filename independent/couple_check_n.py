import random
form = ['1_king'] + [ '2_airplane', '3_eleplant', '4_boat', '5_horse', '6_biggun'] * 2 + ['7_soldier'] * 5
cards = [x+y for y in ['_red', '_black'] for x in form]





 
count_n_tui = [0,0,0,0,0]
n = 100000.0
for round in range(1, int(n)+1):
    random.shuffle(cards)
    players = []
    for i in [0,8,16,24]:
        players.append(cards[i:i+8])
    for i in range(0,4):
        players[i].sort()

        couple_count = players[i].count('2_airplane_red') / 2 \
                        + players[i].count('2_airplane_black') / 2 \
                        + players[i].count('3_eleplant_red') / 2 \
                        + players[i].count('3_eleplant_black') / 2 \
                        + players[i].count('4_boat_red') / 2 \
                        + players[i].count('4_boat_black') / 2 \
                        + players[i].count('5_horse_red') / 2 \
                        + players[i].count('5_horse_black') / 2 \
                        + players[i].count('6_biggun_red') / 2 \
                        + players[i].count('6_biggun_black') / 2 \
                        + players[i].count('7_soldier_red') / 2 \
                        + players[i].count('7_soldier_black') / 2

        count_n_tui[couple_count] += 1
        
print 'no tui --> ' + str(count_n_tui[0] / 4.0 * 100 / n) + ' %'
print 'tui = 1--> ' + str(count_n_tui[1] / 4.0 * 100 / n) + ' %'
print 'tui = 2--> ' + str(count_n_tui[2] / 4.0 * 100 / n) + ' %'
print 'tui = 3--> ' + str(count_n_tui[3] / 4.0 * 100 / n) + ' %'
print 'tui = 4--> ' + str(count_n_tui[4] / 4.0 * 100 / n) + ' %'
print 'mean / people --> ' + str((count_n_tui[1] / 4.0 + 2 * count_n_tui[2] / 4.0 + 3 * count_n_tui[3] / 4.0 + 4 * count_n_tui[4] / 4.0)/float(n))
