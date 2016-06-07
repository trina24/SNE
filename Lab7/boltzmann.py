# -*- coding: utf-8 -*-

import math
import random

class Boltzmann:

    def __init__(self):
        self.x_s = [0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 1.0, 1.0, 0.0, 0.0,
                    0.0, 0.0, 1.0, 0.0, 0.0,
                    0.0, 0.0, 1.0, 0.0, 0.0,
                    0.0, 0.0, 1.0, 0.0, 0.0]

    def create_c(self):
        matrix = [[0 for x in range(25)] for y in range(25)]
        for i in range(25):
            for j in range(25):
                if (i == j):
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = (self.x_s[i] - 0.5) * \
                                   (self.x_s[j] - 0.5)
        return matrix

    def create_w(self):
        matrix = [[0 for x in range(25)] for y in range(25)]
        c = self.create_c()
        for i in range(25):
            for j in range(25):
                matrix[i][j] = 2 * c[i][j]
        return matrix

    def create_theta(self):
        theta = []
        c = self.create_c()
        for i in range(25):
            theta.append(sum(c[i]))
        return theta

    def create_u(self, x):
        theta = self.create_theta()
        w = self.create_w()
        u = []
        for i in range(25):
            u.append(sum(k*l for k,l in zip(w[i],x)) - theta[i])
        return u

    def f(self, arg, temp):
        return 1.0 / (1.0 + math.exp(-(arg/temp)))

    def get_x0(self):
        x = []
        for i in range(25):
            x.append(random.randint(0,1))
        return x

    def get_x(self, x, temp):
        u = self.create_u(x)
        x_ = []
        for i in range(25):
            r = random.uniform(0,1)
            fun = self.f(u[i], temp)
            if (r < fun):
                x_.append(0)
            else:
                x_.append(1)
        return x_

    def update_t(self, t0, t):
        return t0 / (1.0 + math.log(t+1))

    def get_image(self, vec):
        image = []
        for element in vec:
            if (element):
                image.append('*')
            else:
                image.append('-')
        return image
        
    def show(self, vec):
        for i in range(len(vec)):
            if (not i % 5):
                print '\n'
            print vec[i],

class Main:

    bl = Boltzmann()
    x0 = bl.get_x0()
    x = [x0]

    # Zadanie 1.

    for t in range(1, 10):
        temp0 = 1.5
        x_t = bl.get_x(x[t-1], temp0)
        x.append(x_t)
    
    # Zadanie 2.

    '''for t in range(1,10):
        temp0 = 1.5
        T = bl.update_t(temp0, t)
        x_t = bl.get_x(x[t-1], T)
        x.append(x_t)'''

    for element in x:
        bl.show(bl.get_image(element))
        print '\n'
