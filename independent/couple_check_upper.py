import random
form = ['1_king'] + [ '2_airplane', '3_eleplant', '4_boat', '5_horse', '6_biggun'] * 2 + ['7_soldier'] * 5
cards = [x+y for y in ['_red', '_black'] for x in form]

couple_player1 = 0
couple_player2 = 0
couple_player3 = 0
couple_player4 = 0
for round in range(1, 15001):
    random.shuffle(cards)
    players = []
    for i in [0,8,16,24]:
        players.append(cards[i:i+8])
    player_card = ''

    for k in range(1,8):
        for i in range(0,4):
            couple_count = 0
            players[i].sort()
            for j in range(0,4):
                if i == j :
                    continue
    
                if players[i].count('2_airplane_red') == 2 :
                    couple_count += 1
                if players[i].count('2_airplane_black') == 2 :
                    couple_count += 1
                if players[i].count('3_eleplant_red') == 2 :
                    couple_count += 1
                if players[i].count('3_eleplant_black') == 2 :
                    couple_count += 1
                if players[i].count('4_boat_red') == 2 :
                    couple_count += 1
                if players[i].count('4_boat_black') == 2 :
                    couple_count += 1
                if players[i].count('5_horse_red') == 2 :
                    couple_count += 1
                if players[i].count('5_horse_black') == 2 :
                    couple_count += 1
                if players[i].count('6_biggun_red') == 2 :
                    couple_count += 1
                if players[i].count('6_biggun_black') == 2 :
                    couple_count += 1
                if players[i].count('7_soldier_red') == 2 :
                    couple_count += 1
                if players[i].count('7_soldier_black') == 2 :
                    couple_count += 1
    
                if i == 0 :
                    couple_player1 += couple_count
                if i == 1 :
                    couple_player2 += couple_count
                if i == 2 :
                    couple_player3 += couple_count
                if i == 3 :
                    couple_player4 += couple_count
    
print 'player1 tui = ' + str(couple_player1 / 15000.0)
print 'player2 tui = ' + str(couple_player2 / 15000.0)
print 'player3 tui = ' + str(couple_player3 / 15000.0)
print 'player4 tui = ' + str(couple_player4 / 15000.0)
print 'all tui = ' + str((couple_player1 + couple_player2 + couple_player3 + couple_player4) / 15000.0)
print 'mean tui = ' + str((couple_player1 + couple_player2 + couple_player3 + couple_player4) / 4.0 / 15000.0)
