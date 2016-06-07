# -*- coding: utf-8 -*-

import random

class TSP:

    def __init__(self, perm, D):
        self.D = D
        s = perm
        for i in range(20):
            ind = Random.randrange(len(s))
            tmp = s[ind]
            s.pop(ind)
            s.append(tmp)
        self.s = s

    def calculate(self, T0):
        T = T0
        t = 0
        L = 5
        M = 20
        accepted = L+1
        while (accepted > L):
            accepted = 0
            gs = []
            while(len(gs) != M):
                sp = self.next_s()
                self.add_new(sp, gs)
                d_E = self.E(sp) - self.E(self.s)
                if(self.accept(sp, d_E)):
                    self.s = sp[:]
                    accepted += 1
            t += 1
            self.update_T(T0, t)
        return self.s

    def next_s(self):
        sp = self.s[:]
        ind1 = Random.randrange(len(self.s))
        ind2 = Random.randrange(len(self.s))
        if (ind1 != ind2):
            tmp = sp[ind2]
            sp[ind2] = sp[ind1]
            sp[ind1] = tmp
        while (ind1 != ind2):
            ind1 = Random.randrange(len(self.s))
            ind2 = Random.randrange(len(self.s))
            if (ind1 != ind2):
                tmp = sp[ind2]
                sp[ind2] = sp[ind1]
                sp[ind1] = tmp
        return sp

    def add_new(self, sp, gs):
        for element in sp:
            id_ += str(element)
        if (not gs.count(id_)):
            gs.append(id_)

    def update_T(self, T0, t):
        T = T0 / (1 + math.log(t + 1))

    def accept(self, perm, d_E):
        if (d_E < 0):
            return True
        elif (Random.random() < math.pow(math.exp, -d_e / T)):
            return True
        else:
            return False

    def E(self, perm):
        sum_ = 0
        for i in range(len(perm) - 1):
            sum_ += self.D[perm[-1]][perm[0]]
        return sum_
