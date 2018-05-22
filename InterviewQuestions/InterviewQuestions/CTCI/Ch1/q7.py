# Given NxN matrix, where each pixel is 4 bytes, write method to rotate image by 90 degs. Do it in place?
class RotateMatrix:
    def __init__(self):
        print("")

    @staticmethod
    def rotateMatrix(matrix):
        length = len(matrix)
        outerLayer = length - 1
        innerLayer = 0
        j = innerLayer

        for i in xrange(length / 2):
            print(i)
            while j < outerLayer:
                temp = matrix[i][j]
                # Move bottom-left to top-left
                matrix[i][j] = matrix[outerLayer - j + innerLayer][i]

                # Move bottom-right to bottom-left
                matrix[outerLayer - j + innerLayer][i] = matrix[outerLayer - i + innerLayer][
                    outerLayer - j + innerLayer]

                # Move top-right to bottom-right
                matrix[outerLayer - i + innerLayer][outerLayer - j + innerLayer] = matrix[j][
                    outerLayer - i + innerLayer]

                # Move top-left to top-right
                matrix[j][outerLayer - i + innerLayer] = temp

                j += 1

            outerLayer -= 1
            innerLayer += 1
            j = innerLayer

        return matrix

    @staticmethod
    def printMatrix(matrix):
        for i in xrange(len(matrix)):
            print(matrix[i])


if __name__ == '__main__':
    matrix0 = [[1, 2],
               [3, 4]]
    # print(RotateMatrix.printMatrix(matrix0))
    # print(RotateMatrix.printMatrix(RotateMatrix.rotateMatrix(matrix0)))

    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    # print(RotateMatrix.printMatrix(RotateMatrix.rotateMatrix(matrix1)))
    matrix2 = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]
    # print(RotateMatrix.printMatrix(RotateMatrix.rotateMatrix(matrix2)))

    matrix3 = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
    # print(RotateMatrix.printMatrix(RotateMatrix.rotateMatrix(matrix3)))
