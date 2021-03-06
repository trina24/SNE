# -*- coding: utf-8 -*-

import random
import math

class Tsp:

    def __init__(self, temp0, M, L):
        self.temp0 = temp0
        self.t = 0
        self.s = [i+1 for i in range(10)]
        random.shuffle(self.s)
        self.M = M
        self.L = L
        self.accepted = 0
        self.accepted_lst = []

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
                    self.accepted_lst.append(s)
            self.update()
        return gen

    def dist(self, a, b):
        if ((a == 1 and b == 10) or (a == 10 and b == 1)):
            return 1
        else:
            return abs(a-b)

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
        self.temp = self.temp0 / (1 + math.log(self.t + 1))

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
    tsp.algorithm()
    gen = tsp.accepted_lst
    best = tsp.find_min(gen)
    for element in gen:
        print element
    print "\nbest: " + str(best[0])
    print "expense: " + str(best[1])
