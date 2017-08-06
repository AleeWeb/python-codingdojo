
import random

def tossCoins():
    head = 0
    tail = 0
    for i in range(5000):
        if round(random.random()) == 0.0:
            tail += 1
            print 'Attempt #', i, \
                ": Throwing a coin...It's a tail!...Got ", head, \
                ' head(s) so far and ', tail, ' tail(s) so far'
        else:
            head += 1
            print 'Attempt #', i, \
                ": Throwing a coin...It's a head!...Got ", head, \
                ' head(s) so far and ', tail, ' tail(s) so far'
    print 'Ending the program, thank you!'


tossCoins()