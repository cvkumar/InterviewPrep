def findFirstGreaterOrEqual(nums, target):
    lower = 0
    upper = len(nums) - 1

    while lower <= upper:
        mid = (lower + upper) / 2
        # print lower, mid, upper
        if nums[mid] < target:
            # Look Right
            lower = mid + 1
        else:
            # Look Left
            upper = mid - 1

    return lower


def findFirstLesserOrEqual(nums, target):
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

    return lower - 1


def countScores(lowerLimits, upperLimits, scores):
    """
    Given lowerLimits, upperLimits, and scores. For each range, find the number of scores (inclusively) within the range.
    """
    scores.sort()
    # print(scores)
    results = []

    for i in range(len(lowerLimits)):
        lower = findFirstGreaterOrEqual(scores, lowerLimits[i])
        upper = findFirstLesserOrEqual(scores, upperLimits[i])
        # print "lower: {}, upper: {}".format(lower, upper)
        results.append(upper - lower + 1)

    return results


if __name__ == '__main__':
    # Binary Search Test
    nums = [0, 5, 10, 13, 16]
    # print(findBSIndex(nums, 15, 0, len(nums)))

    # findLeastGreaterTests
    test = [0, 5, 10, 12, 15]
    # print(findFirstGreaterOrEqual(test, 12))
    # print(findFirstLesserOrEqual(test, -1))

    # TESTCASE 1
    lowerLimits = [2, 3, 0]
    upperLimits = [6, 6, 12]
    scores = [0, 3, 6, 9, 12]
    print(countScores(lowerLimits, upperLimits, scores))
    # Expected [2, 2, 5]

    # TESTCASE 2
    lowerLimits = [3, 6, 5]
    upperLimits = [13, 10, 13]
    scores = [0, 5, 10, 12, 15]
    # Expected [3, 1, 3]
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
