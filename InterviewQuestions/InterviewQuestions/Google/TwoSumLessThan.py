"""
PROBLEM:
Check if any two values in array sum to less than target
"""

"""
nLog(n) Solution

Algorithm:
Sort array, see if first two entries sum to less than target
"""

"""

"""

def checkSumToLess(nums, target):
    print 'h'


if __name__ == '__main__':
    nums = [5, 2, 4, 8, 1]
    t = 4
    assert checkSumToLess(nums, t) == True

    nums = [-1, 1, 5, 2, 0]
    t = -1
    assert checkSumToLess(nums, t) == False

    nums = []
    assert checkSumToLess(nums, t) == False

