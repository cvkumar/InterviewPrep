import operator


def countScores(lowerLimits, upperLimits, scores):
    """
    Given lowerLimits, upperLimits, and scores. For each range, find the number of scores (inclusively) within the range.
    """
    scores.sort()
    # print(scores)
    results = []

    for i in range(len(lowerLimits)):
        lower = findLeastGreater(scores, lowerLimits[i])
        upper = findLeastGreater(scores, upperLimits[i])
        results.append(upper - lower)

    return results


def findLeastGreater(nums, target):
    lower = 0
    upper = len(nums) - 1

    while lower <= upper:
        mid = (lower + upper) / 2
        # print lower, mid, upper
        if nums[mid] <= target:
            # Look Right
            lower = mid + 1
        else:
            # Look Left
            upper = mid - 1

    return lower


def findGreatestLesser(nums, target):
    lower = 0
    upper = len(nums) - 1

    while lower < upper:
        mid = (lower + upper) / 2
        # print lower, mid, upper
        if nums[mid] <= target:
            # Look Right
            lower = mid + 1
        else:
            # Look Left
            upper = mid

    return lower


if __name__ == '__main__':
    # Binary Search Test
    nums = [0, 5, 10, 13, 16]
    # print(findBSIndex(nums, 15, 0, len(nums)))

    # findLeastGreaterTests
    test = [0, 5, 10, 12, 15]
    # print(findLeastGreater(test, 14))
    # print(findGreatestLesser(test, 6))

    # TESTCASE 1
    lowerLimits = [0, 5, 10]
    upperLimits = [10, 15, 12]
    scores = [15, 0, 5, 10, 12]
    print(countScores(lowerLimits, upperLimits, scores))
    # Expected [3, 4, 2]

    # TESTCASE 2
    lowerLimits = [3, 6, 5] # 1
    upperLimits = [13, 10, 13] # 4
    scores = [0, 5, 10, 12, 15]
    #   Expected [3, 1, 3]
    print(countScores(lowerLimits, upperLimits, scores))


# https://stackoverflow.com/questions/6553970/find-the-first-element-in-a-sorted-array-that-is-greater-than-the-target?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


def binarySearch(nums, target, lower, upper):
    if lower > upper:
        # print(upper, lower)
        return -1
    mid = (lower + upper) / 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        # Look Left
        return binarySearch(nums, target, lower, mid - 1)
    else:
        # Look Right
        return binarySearch(nums, target, mid + 1, upper)
