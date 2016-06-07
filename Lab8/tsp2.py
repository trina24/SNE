# -*- coding: utf-8 -*-

import random
import math

class Tsp:

    def __init__(self, temp0, M, L):
        self.temp0 = temp0
        self.temp = temp0
        self.s = [i+1 for i in range(10)]
        random.shuffle(self.s)
        self.M = M
        self.L = L
        self.accepted = 0

    def algorithm(self):
        while (self.accepted <= self.L):
            gen = []
            self.accepted = 0
            while (len(gen) < self.M):
                s = self.gen_new(self.s)
                gen.append(s)
                diff = self.expense(s) - self.expense(self.s)
                if (self.accept(s, diff)):
                    self.s = s
                    self.accepted += 1
            self.update()
        return gen

    def dist(self, a, b):
        if ((a == 1 and b == 2) or (a == 9 and b == 10)):
            return 1
        elif (a < b):
            return math.pow(a,3) + math.pow(b,3) - a * math.pow(b,2) + 4 * math.pow(a,2) - \
              4 * math.pow(b,2) + 4 * a + 4 * b
        elif (a > b):
            return self.dist(b, a)
        else:
            return 0

    def expense(self, s):
        exp = 0
        for i in range(9):
            exp += self.dist(s[i], s[i+1])
        exp += self.dist(s[9],s[0])
        return exp

    def gen_new(self, s):
        r1 = random.randint(0, len(s) - 1)
        r2 = random.randint(0, len(s) - 1)
        while (r1 == r2):
            r2 = random.randint(0, len(s) - 1)
        new_s = s[:]
        new_s[r1], new_s[r2] = new_s[r2], new_s[r1]
        return new_s

    def accept(self, s, diff):
        if (diff < 0):
            return True
        else:
            r = random.random()
            return r < math.exp(-diff / self.temp)

    def update(self):
        self.temp = self.temp0 / (1 + math.log(self.temp + 1))

    def find_min(self, gen):
        min_exp = self.expense(gen[0])
        min_sol = gen[0]
        for element in gen:
            if (self.expense(element) < min_exp):
                min_exp = self.expense(element)
                min_sol = element
        return (min_sol, min_exp)

class Main:

    tsp = Tsp(10, 10, 3)
    gen = tsp.algorithm()
    best = tsp.find_min(gen)
    for element in gen:
        print element
    print "\nbest: " + str(best[0])
    print "expense: " + str(best[1])
