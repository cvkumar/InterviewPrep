def isRectangleBruteForce(grid):
    for i in range(0, len(grid) - 1):
        columnsWithOne = []
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1:
                if formRectangle(grid, i, j, columnsWithOne):
                    return True
                else:
                    columnsWithOne.append(j)

    return False


def formRectangle(grid, i, j, columnsWithOne):
    # print i, j
    for k in range(len(columnsWithOne)):
        for runner in range(i + 1, (len(grid))):
            if grid[runner][j] == 1 and grid[runner][columnsWithOne[k]] == 1:
                # print "runner: {} columnsWithOne[k]: {} j: {}".format(runner, columnsWithOne[k], j)
                return True
    return False


if __name__ == '__main__':
    grid = [[1, 1, 1],
            [0, 0, 0],
            [0, 1, 1]]

    print(isRectangleBruteForce(grid))
    grid2 = [[1, 0],
             [1, 1]]
    print(isRectangleBruteForce(grid2))

    grid3 = [[1, 1, 1, 1],
             [0, 0, 0, 0],
             [1, 0, 0, 1],
             [0, 0, 0, 1]]

    print(isRectangleBruteForce(grid3))
