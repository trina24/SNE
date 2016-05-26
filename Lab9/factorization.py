# -*- coding: utf-8 -*-

import random
import math

class Factorization:
    
    def gcd(self, a, b):
        if (a % b == 0):
            return b
        else:
            return self.gcd(b, a % b)

    def discrete_log(self, N):
        a = random.randint(1, N-1)
        if (self.gcd(N,a) > 1):
            return self.gcd(N,a)
        else:
            r = 2
            while (self.gcd(N, math.pow(a,r/2) + 1) == 1 and self.gcd(N, math.pow(a,r/2) - 1) == 1):
                r += 1
            if (self.gcd(N, math.pow(a,r/2) + 1) != 1):
                return self.gcd(N, math.pow(a,r/2) + 1)
            else:
                return self.gcd(N, math.pow(a,r/2) - 1)
class Main:

    N = [12, 91, 143, 1737, 1859]
    fc = Factorization()
    for element in N:
        print 'for N = ' + str(element) + ': ' + str(fc.discrete_log(element))
    flag = False
    while (flag == False):
        try:
            print 'for N = 988027: ' + str(fc.discrete_log(988027))
            flag = True
        except OverflowError:
            pass
