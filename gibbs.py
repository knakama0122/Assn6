import random

class Query:

    def __init__(self):
        self.result = 0
        self.c = False
        self.s = False
        self.w = False
        self.r = False

    def simulate(self):
        cRandom = random.random()
        sRandom = random.random()
        wRandom = random.random()
        rRandom = random.random()

        if cRandom < 0.5:
            self.c = True
            if sRandom < 0.1: self.s = True
            if rRandom < 0.8: self.r = True
        else: # c > 0.5
            if sRandom < 0.5: self.s = True
            if rRandom < 0.2: self.r = True

        if self.s == True:
            if self.r == True:
                if wRandom < 0.99:
                    self.w = True
            else:
                if wRandom < 0.9:
                    self.w = True
        else:
            if self.r == True:
                if wRandom < 0.9:
                    self.w = True
            else:
                if wRandom < 0:
                    self.w = True
        if self.s == False:
            if self.w == True:
                if self.c == True:
                    self.result = 1
                else:
                    self.result = 2




if __name__ == "__main__":
    print("Part A. The sampling probabilities")
    print("P(C| -s, r) = 〈0.87804,0.12195〉")
    print("P(C| -s, -r) = 〈0.310345,0.689655〉")
    print("P(R| c, -s, w) = 〈1,0〉") 
    print("P(R| -c, -s, w) = 〈1,0〉")
    print("\n Part B. The transition probability matrix")
    print("      S1         S2         S3         S4") 
    print("S1    0.3448275  0.5        0.1551725  0")   
    print("S2    0          0.560975   0          0.439025") 
    print("S3    0.3448275  0          0.1551725  0.5") 
    print("S4    0          0.060975   0          0.939025") 
    cTrueCount = 0
    cFalseCount = 0

    for i in range(1000000):
        query = Query()
        query.simulate()
        if query.result == 1:
            cTrueCount += 1
        elif query.result == 2:
            cFalseCount += 1

    cTrue = cTrueCount / (cTrueCount + cFalseCount)
    cFalse = cFalseCount / (cTrueCount + cFalseCount)

    print("\nPart C. The probability of the query")
    print("P(C|-s,w) = <", "{0:.6f}".format(cTrue) , " ", "{0:.6f}".format(cFalse), ">")
