# -*- coding: utf-8 -*-

import math

eps = 0.00001
c = 0.01

def f1(x, y, z):
    return 2 * math.pow(x, 2) + 2 * math.pow(y, 2) + math.pow(z, 2) - 2 * x * y - 2 * y * z - 2 * x + 3

def f2(x, y):
    return 3 * math.pow(x, 4) + 4 * math.pow(x, 3) - 12 * math.pow(x, 2) + 12 * math.pow(y, 2) - 24 * y

def derf1(i, x, y, z):
    if i == 0:
        return 4 * x - 2 * y - 2
    elif i == 1:
        return 4 * y - 2 * x - 2 * z
    else:
        return 2 * z - 2 * y

def derf2(i, x, y):
    if i == 0:
        return 12 * math.pow(x, 3) + 12 * math.pow(x, 2) - 24 * x
    else:
        return 24 * y - 24

def minf1():
    start = [0, 0, 1]

    vec_old = start
    vec_new = [0, 0, 0]

    for i in range(len(vec_new)):
        vec_new[i] = vec_old[i] - c * derf1(i, vec_old[0], vec_old[1], vec_old[2])

    while (max(abs(x - y) for x, y in zip(vec_new, vec_old)) > eps):
        vec_old = list(vec_new)
        for i in range(len(vec_new)):
            vec_new[i] = vec_old[i] - c * derf1(i, vec_old[0], vec_old[1], vec_old[2])

    else:
        return vec_new

def minf2():
    start = [4, 2]

    vec_old = start
    vec_new = [0, 0]

    for i in range(len(vec_new)):
        vec_new[i] = vec_old[i] - c * derf2(i, vec_old[0], vec_old[1])

    while (max(abs(x - y) for x, y in zip(vec_new, vec_old)) > eps):
        vec_old = list(vec_new)
        for i in range(len(vec_new)):
            vec_new[i] = vec_old[i] - c * derf2(i, vec_old[0], vec_old[1])

    else:
        return vec_new

print '\n'

print 'min f:'
print 'v = ' + str(minf1())
print 'f(v) = ' + str(f1(minf1()[0],minf1()[1],minf1()[2]))

print '\n'

print 'min g:'
print 'v = ' + str(minf2())
print 'g(v) = ' + str(f2(minf2()[0],minf2()[1]))
