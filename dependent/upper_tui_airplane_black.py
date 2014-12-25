import random
n = 10000.0
event = 0.0
for round in range(1, int(n+1)):
    form = ['1_king'] + [ '2_airplane', '3_eleplant', '4_boat', '5_horse', '6_biggun'] * 2 + ['7_soldier'] * 5
    cards = [x+y for y in ['_red', '_black'] for x in form]

    cards.remove('2_airplane_black')
    cards.remove('2_airplane_black')
    cards.remove('2_airplane_red')
    cards.remove('2_airplane_red')

    random.shuffle(cards)
    cards = ['2_airplane_black'] * 2 + cards + ['2_airplane_red'] * 2
    players = []
    players.append(cards[0:8])
    players[0].sort()
    cards = cards[8:32]
    random.shuffle(cards)
    for i in [0,8,16]:
        players.append(cards[i:i+8])

    for i in range(0,4):
        line_output = ''
        if players[i].count('2_airplane_red') == 2 :
            event += 1
        for x in players[i]:
            line_output += x + ' '
        print 'player ' + str(i+1) + ' ---> ' + line_output
    print '===================================================================================================================================='

print 'event ' + str(event)
print 'samplespace ' + str(n)
print str(event / n * 100) + ' %'
