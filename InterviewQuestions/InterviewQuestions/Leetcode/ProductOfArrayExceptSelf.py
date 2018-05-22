class ProductOfArrayExceptSelf:
    def __init__(self):
        print("")

    @staticmethod
    def createProductOfArrayExceptSelf(nums):
        nums_length = len(nums)
        right = [0] * nums_length
        left = []
        result = []

        left.append(1)
        right[nums_length - 1] = 1

        for i in xrange(1, nums_length):
            left.append(left[i - 1] * nums[i - 1])

        for i in xrange(nums_length - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]

        for i in xrange(0, nums_length):
            result.append(right[i] * left[i])

        print(result)


if __name__ == '__main__':
    ProductOfArrayExceptSelf.createProductOfArrayExceptSelf([1, 2, 3, 4])
