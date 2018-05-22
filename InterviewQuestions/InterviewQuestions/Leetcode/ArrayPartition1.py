# Given an array of 2n integers, your task is to group these integers into n pairs of integer,
# say (a1, b1), (a2, b2), ...,
# (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

class ArrayPartition1:
    def __init__(self):
        print ""

    @staticmethod
    def arrayPairSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    print(ArrayPartition1.arrayPairSum(nums))  # 4
