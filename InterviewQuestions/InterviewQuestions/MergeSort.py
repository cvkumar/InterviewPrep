def mergeSort(nums, low, high):
    """

    :param nums: array to be sorted
    :param low: points first element
    :param high: points out of bounds on right side
    :return: sorted array
    """
    mid = (low + high) / 2


    t = mergeSort(nums, low, mid)
    t2 = mergeSort(nums, mid + 1, high)

    # TODO: Return indices that point to beginning of merged stuff

    # return merge()




def merge(nums, l, m, h):
    """
    :param l: points to leftmost element
    :param m: points to last element of left half
    :param h: points to out of bounds of right half
    :return: sorts sub-array from l to h
    """
    ptr1 = l
    ptr2 = m + 1

    res = []

    while ptr1 < m and ptr2 < h:
        if nums[ptr1] < nums[ptr2]:
            res.append(nums[ptr1])
            ptr1 += 1
        else:
            res.append(nums[ptr2])
            ptr2 += 1

    while ptr1 <= m:
        res.append(nums[ptr1])
        ptr1 += 1

    while ptr2 < h:
        res.append(nums[ptr2])
        ptr2 += 1

    j = 0
    for i in range(l, h):
        nums[i] = res[j]
        j += 1

    return nums


if __name__ == '__main__':
    arr1 = [1, 3, 5, 10, 2, 3, 7, 11]

    print(merge(arr1, 0, 3, len(arr1)))
