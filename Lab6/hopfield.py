# -*- coding: utf-8 -*-

import math
import random

class Hopfield:

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

    def get_x0(self):
        x = []
        for i in range(25):
            x.append(random.randint(0,1))
        return x

    def get_x(self, t, x):
        u = self.create_u(x)
        x_ = []
        for i in range(25):
            if (u[i] > 0):
                x_.append(1)
            elif (u[i] == 0):
                return self.get_x(t-1, x)
            else:
                x_.append(0)
        return x_

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

    hp = Hopfield()
    x0 = hp.get_x0()
    x = [x0]
    
    for t in range(1,4):
        x_t = hp.get_x(t, x[t-1])
        x.append(x_t)

    for element in x:
        hp.show(hp.get_image(element))
        print '\n'
