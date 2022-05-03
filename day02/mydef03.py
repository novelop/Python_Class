from random import random

def myrandom():
    rnd = random.random() 
    if rnd > 0.5:
        return 1
    else: 
        return 0
    #return int(random.random() * 2)


rnd = myrandom()
print("rnd",rnd)