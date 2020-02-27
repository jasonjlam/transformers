import math

#print the matrix such that it looks like
#the template in the top comment
def printMatrix( matrix ):
    print ("-" * 2 * len(matrix))
    for r in range(0,4):
        for c in range(0, len(matrix)):
            # print("{}, {}".format(r,c))
            print(str(matrix[c][r]) + " ", end = '')
            if (c == len(matrix) - 1):
                print("")
    print ("-" * 2 * len(matrix))

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def identity( matrix ):
    for c in range(0, len(matrix)):
        for r in range(0, len(matrix[c])):
            if c == r:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrixMulti( m1, m2 ):
    for c in range(0, len(m2)):
        temp = []
        for r in range(0, 4):
            # print ("{},{}".format(c,r))
            i = 0
            for x in range(0,4):
                # print("{}*{}".format(m1[x][r], m2[c][x]))
                i += (m1[x][r] * m2[c][x])
                # print(i)
            temp.append(i)
        m2[c] = temp


def newMatrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def addPoint(matrix, x, y, z= 0):
    matrix.append([x,y,z, 1])
