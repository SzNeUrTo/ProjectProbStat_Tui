import random
form = ['1_king'] + [ '2_airplane', '3_eleplant', '4_boat', '5_horse', '6_biggun'] * 2 + ['7_soldier'] * 5
cards = [x+y for y in ['_red', '_black'] for x in form]

n = 1000000.0
dependent_sample_space = 0.0
sum = 0
for round in range(1, int(n+1)):
    random.shuffle(cards)
    players = []
    for i in [0,8,16,24]:
        players.append(cards[i:i+8])

    have_hoo = False
    hoo_big_have_index = -1
    for i in range(0,4):
        players[i].sort()
        #print players[i]
        if players[i].count('1_king_black') == 1:
            if (players[i].count('2_airplane_black') == 2 and players[i].count('3_eleplant_black') == 1) \
            or (players[i].count('2_airplane_black') == 1 and players[i].count('3_eleplant_black') == 2):
                if (players[i].count('2_airplane_red') <= 1 and players[i].count('3_eleplant_red') == 0) \
                or (players[i].count('2_airplane_red') == 0 and players[i].count('3_eleplant_black') <= 1):
                    have_hoo = True
                    dependent_sample_space += 1
                    hoo_big_have_index = i

    for i in range(0,4):
        text_list = ''
        for x in players[i]:
            text_list += x + ' '
        print 'player ' + str(i+1) + ' ---> ' + text_list

    print '===================================================================================================================================='
    if have_hoo :
        i = hoo_big_have_index
        for j in range(0,4):
            if i == j:
                continue
            if players[j].count('1_king_red') == 1:
                if (players[j].count('2_airplane_red') >= 2 and players[j].count('3_eleplant_red') >= 1) \
                or (players[j].count('2_airplane_red') >= 1 and players[j].count('3_eleplant_red') >= 2):
                    sum += 1
    

print '===================================================================================================================================='
print 'dependent_sample_space ' + str(dependent_sample_space)
print 'sum ' + str(sum)
percent = sum / dependent_sample_space * 100
print str(percent) + ' %'
percent /= 4.0
print str(percent) + ' %'
