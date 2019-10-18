import math
import random
class Pi:
    def __init__(self, exp):
        self.exp = exp
        self.pi = 0

    def simluation(self):
        count = 0
        trial = 10 ** self.exp
        for x in range(trial):
            x = random.random()
            y = random.random()
            d = x ** 2 + y ** 2
            if d < 1.0:
                count = count + 1
        self.pi = count / trial * 4
    
    def print(self):
        print('n = 10 ^ ', self.exp, " pi = ", "{0:.6f}".format(self.pi), 
        "{0:.4f}".format((abs((self.pi)- math.pi) / math.pi)* 100), " %")

if __name__ == '__main__':
    for i in range(3,7):
        pi = Pi(i)
        pi.simluation()
        pi.print()

