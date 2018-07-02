def mergeSort(nums, low, high):
    """
    :param nums: array to be sorted
    :param low: points first element
    :param high: points out of bounds on right side
    :return: sorted array
    """
    if low >= high:
        return

    # mid points to mid element (rounds down if necessary)
    mid = (low + high - 1) / 2

    mergeSort(nums, low, mid)
    mergeSort(nums, mid + 1, high)
    merge(nums, low, mid, high)


def merge(nums, l, m, h):
    """
    :param nums: array to be sorted
    :param l: points to leftmost element
    :param m: points to last element of left half
    :param h: points to out of bounds of right half
    :return: sorts sub-array from l to h
    """
    ptr1 = l
    ptr2 = m + 1

    res = []

    while ptr1 <= m and ptr2 < h:

        if nums[ptr1] < nums[ptr2]:
            res.append(nums[ptr1])
            ptr1 += 1
        else:
            res.append(nums[ptr2])
            ptr2 += 1

    # print res

    while ptr1 <= m:
        res.append(nums[ptr1])
        ptr1 += 1

    while ptr2 < h:
        res.append(nums[ptr2])
        ptr2 += 1

    j = 0
    for i in range(l, h):
        # print i, j
        nums[i] = res[j]
        j += 1

    print 'sorted array from {} to {}'.format(l, h - 1)
    print nums

    return nums


if __name__ == '__main__':
    nums = [1, 3, 5, 10, 2, 3, 7, 11]

    # print merge(nums, 0, 3, len(nums))

    arr2 = [5, 1, 3, 8, 10, 0, 4, 3]
    mergeSort(arr2, 0, len(arr2))
    print arr2
