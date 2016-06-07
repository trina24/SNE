# -*- coding: utf-8

import math

class Propagation:

    def __init__(self):
        self.eps = 0.000001
        self.c = 0.1
        self.beta = 2.5

        self.u = [[0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
        self.z = [0, 1, 1, 0]

    def f(self, arg):
        return 1.0 / (1.0 + math.exp(-self.beta * arg))

    def der_f(self, arg):
        return self.beta * self.f(arg) * (1.0 - self.f(arg))

    def calc_x(self, w):
        x = []
        for i in range(len(self.u)):
            x1 = self.f(sum(k*l for k, l in zip(w[0], self.u[i])))
            x2 = self.f(sum(k*l for k, l in zip(w[1], self.u[i])))
            x.append([x1, x2, 1])
        return x

    def calc_y(self, x, s):
        y = []
        for i in range(len(x)):
            yp = self.f(sum(k*l for k,l in zip(s, x[i])))
            y.append(yp)
        return y
    
    def der_E_s(self, x, y, s):
        der = []
        for i in range(3):
            temp = 0
            for p in range(4):
                temp += (y[p] - self.z[p]) * \
                        self.der_f(sum(k*l for k,l in \
                                       zip(s, x[p]))) * x[p][i]
            der.append(temp)
        return der

    def der_E_w(self, x, y, s, w):
        der = []
        for i in range(2):
            row = []
            for j in range(3):
                temp = 0
                for p in range(4):
                    temp += (y[p] - self.z[p]) * self.der_f(sum(k*l for k, l in zip(s, x[p]))) * s[i] * self.der_f(sum(k*l for k, l in zip(w[i], self.u[p]))) * self.u[p][j]
                row.append(temp)
            der.append(row)
        return der

    def get_s(self, old, der):
        s = []
        for i in range(3):
            temp = old[i] - self.c * der[i]
            s.append(temp)
        return s

    def get_w(self,old, der):
        w = []
        for i in range(2):
            row = []
            for j in range(3):
                temp = old[i][j] - self.c * der[i][j]
                row.append(temp)
            w.append(row)
        return w

    def propagate(self):
        s_t = [[0,1,2]]
        w_t = [[[0,1,2],[0,1,2]]]

        x = self.calc_x(w_t[0])
        y = self.calc_y(x, s_t[0])
        der_s = self.der_E_s(x, y, s_t[0])
        der_w = self.der_E_w(x, y, s_t[0], w_t[0])

        s_t.append(self.get_s(s_t[0], der_s))
        w_t.append(self.get_w(w_t[0], der_w))
        t = 1

        while(max(max(abs(old - new) for old, new in \
                  zip(s_t[t], s_t[t-1])),
              max(abs(old - new) for old, new in \
                  zip(w_t[t][0], w_t[t-1][0])),
              max(abs(old - new) for old, new in \
                  zip(w_t[t][1], w_t[t-1][1]))) > self.eps):
        
            print max(max(abs(old - new) for old, new in \
                          zip(s_t[t], s_t[t-1])),
              max(abs(old - new) for old, new in \
                  zip(w_t[t][0], w_t[t-1][0])),
              max(abs(old - new) for old, new in \
                  zip(w_t[t][1], w_t[t-1][1])))

            x = self.calc_x(w_t[t])
            y = self.calc_y(x, s_t[t])
            der_s = self.der_E_s(x, y, s_t[t])
            der_w = self.der_E_w(x, y, s_t[t], w_t[t])
        
            s_t.append(self.get_s(s_t[t], der_s))
            w_t.append(self.get_w(w_t[t], der_w))
            t += 1
        
        print "\nZadanie 1:"
        print w_t[t]
        print s_t[t]
        print "\nZadanie 2:"
        print y

class Main:

    pr = Propagation()
    pr.propagate()
