# -*- coding: utf-8 -*-

class Association:

    def __init__(self):
        self.z0 = [ -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1,\
 -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1]
        self.z1 = [ -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, \
-1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1]
        self.z0_ = [ -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, \
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.z1_ = [ -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, \
-1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1]

    def show(self, vector):
        matrix = []
        for element in vector:
            if (element == -1):
                matrix.append('-')
            elif (element == 1):
                matrix.append('*')
            else:
                print 'Matrix elements must be 1 or -1'
                return
        for i in range(len(matrix)):
            if not i % 5:
		print '\n'
            print matrix[i],
        print '\n'

    def define_matrix(self, vec1, vec2):
        matrix = [[0 for x in range(25)] for y in range(25)]  
	for i in range(25):
            for j in range(25):
                matrix[i][j] = 0.04 * (vec1[i] * vec1[j] + vec2[i] * \
vec2[j])
	return matrix

    def sgn(self, x):
	if x >= 0:
            return 1
	else:
            return -1

    def SGN(self, vector):
	sgn_vector = []
	for i in range(25):
            sgn_vector.append(self.sgn(vector[i]))
	return sgn_vector

    def function(self, matrix, vector):
	fu = [0 for i in range(25)]
	for i in range(25):
            for j in range(25):
                fu[i] += matrix[i][j] * vector[j]
	return self.SGN(fu)

class Main:

        assoc = Association()
        w = assoc.define_matrix(assoc.z0, assoc.z1)

        print 'z0:'
        assoc.show(assoc.z0)
        print 'F(z0):'
        assoc.show(assoc.function(w, assoc.z0))

        print 'z1:'
        assoc.show(assoc.z1)
        print 'F(z1):'
        assoc.show(assoc.function(w, assoc.z1))

        print 'Zaburzone z0:'
        assoc.show(assoc.z0_)
        print 'Zaburzone F(z0):'
        assoc.show(assoc.function(w, assoc.z0_))

        print 'Zaburzone z1:'
        assoc.show(assoc.z1_)
        print 'Zaburzone F(z1):'
        assoc.show(assoc.function(w, assoc.z1_))
        
