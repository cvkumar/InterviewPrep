# If 0 in matrix set entire row and column to zero
class ZeroMatrix:
    def __init__(self):
        print("")

    def printMatrix(self, matrix):
        for i in xrange(len(matrix)):
            print(matrix[i])
        print('\n')

    def zeroifyMatrix(self, matrix):
        length = len(matrix)
        zeroRows = {}
        zeroColumns = {}

        for i in xrange(length):
            for j in xrange(length):
                if matrix[i][j] == 0:
                    zeroRows[i] = True
                    zeroColumns[j] = True
                else:
                    if i not in zeroRows:
                        zeroRows[i] = False
                    if j not in zeroColumns:
                        zeroColumns[j] = False

        # print(zeroRows)
        # print(zeroColumns)
        for i in xrange(length):
            if zeroRows[i]:
                # print "set row: " + str(i) + " to zeroes"
                for j in xrange(length):
                    matrix[i][j] = 0

        for j in xrange(length):
            if zeroColumns[j]:
                # print "set column: " + str(j) + " to zeroes"
                for i in xrange(length):
                    matrix[i][j] = 0

        self.printMatrix(matrix)


if __name__ == '__main__':
    zeroMatrix = ZeroMatrix()
    matrix0 = [[1, 2],
               [3, 0]]
    zeroMatrix.zeroifyMatrix(matrix0)

    matrix1 = [[0, 2, 3],
               [4, 1, 6],
               [0, 8, 9]]
    zeroMatrix.zeroifyMatrix(matrix1)

    matrix2 = [[1, 2, 3, 4],
               [5, 0, 0, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]
    zeroMatrix.zeroifyMatrix(matrix2)

    matrix3 = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
