def countScores(lowerLimits, upperLimits, scores):
    """
    Given lowerLimits, upperLimits, and scores. For each range, find the number of scores (inclusively) within the range.
    """
    scores.sort()
    # print(scores)
    results = []

    for i in range(len(lowerLimits)):
        lower = findBSIndex(scores, lowerLimits[i], 0, len(scores) - 1)
        upper = findBSIndex(scores, upperLimits[i], 0, len(scores) - 1)
        results.append(upper - lower + 1)

    return results


def findBSIndex(nums, target, lower, upper):
    if lower > upper:
        # print(upper, lower)
        if nums[lower] < target:
            return lower
        else:
            return lower
    mid = (lower + upper) / 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        # Look Left
        return findBSIndex(nums, target, lower, mid - 1)
    else:
        # Look Right
        return findBSIndex(nums, target, mid + 1, upper)


if __name__ == '__main__':
    # Binary Search Test
    nums = [0, 5, 10, 12, 15]
    # print(findBSIndex(nums, 15, 0, len(nums)))

    # TESTCASE 1
    lowerLimits = [0, 5, 10]
    upperLimits = [10, 15, 12]
    scores = [15, 0, 5, 10, 12]
    print(countScores(lowerLimits, upperLimits, scores))
    # Expected [3, 4, 2]

    # TESTCASE 2
    lowerLimits = [3, 6, 5]
    upperLimits = [13, 10, 13]
    scores = [0, 5, 10, 12, 15]

    #   Expected [3, 1, 3]
    # print(countScores(lowerLimits, upperLimits, scores))


# https://stackoverflow.com/questions/6553970/find-the-first-element-in-a-sorted-array-that-is-greater-than-the-target?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa