# -*- coding: utf-8 -*-

class Perceptron:

    def __init__(self, vecU, vecW):
        self.vecU = vecU
        self.vecW = vecW
        self.time = 1

    def learn(self, constant):
        nextW = self.vecW
        t = 1
        counter = 0
        while (counter != 5):
            ind = (t - 1) % 5
            if (ind < 3):
                z = 1
            else:
                z = 0
            y = self.if_nonnegative(self.scalar_product(nextW, self.vecU[ind]))
            if (z != y):
                for i in range(len(self.vecW)):
                    nextW[i] += constant * (z - y) * self.vecU[ind][i]
            t += 1
            if (z == y):
                counter += 1
            else:
                counter = 0
        self.time = t
        self.vecW = nextW
            

    def scalar_product(self, vector1, vector2):
        sp = 0
        for i in range(len(vector2)):
            sp += vector1[i] * vector2[i]
        return sp

    def if_nonnegative(self, number):
        if (number >= 0):
            return 1
        else:
            return 0

class Main:

    U1 = [0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1]
    U2 = [0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    U3 = [0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1]
    U4 = [0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1]
    U5 = [0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1]
    W = [1 for i in range(26)]

    U = [U1, U2, U3, U4, U5]
    per = Perceptron(U, W)

    constant = float(raw_input("Podaj c: \n"))

    per.learn(constant)

    toprint = ["%.2f" % element for element in per.vecW]

    print 't = ' + str(per.time) + '\n'
    print 'w = ' + str(toprint) + '\n'
