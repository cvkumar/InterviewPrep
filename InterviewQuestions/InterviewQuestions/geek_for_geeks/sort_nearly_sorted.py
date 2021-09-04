"""
Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time.
For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
            k = 3
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
         k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}

"""


def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp


def sort_nearly_sorted_attempt(arr: list, k: int):
    """
    This algorithm doesnt work and should've been thought through more


    """
    for i in range(len(arr)):
        print(arr)
        j = 1
        found_index = None
        while j <= k and i + j < len(arr):
            if arr[i] > arr[j]:
                found_index = j
            j += 1

        print(i, found_index)
        if found_index:
            temp = arr[i]
            arr[i] = arr[found_index]
            arr[found_index] = temp


def insertion_sort_solution(arr: list, k: int):
    """
    Each element has to move in the worst case at most k times so O(nk) solution

    """

    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        curr_element = arr[i]
        j = i - 1

        while curr_element < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = curr_element


print("Insertion Sort Solution")
arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
print(arr)
insertion_sort_solution(arr, k)
print(arr)

print()

arr = [10, 9, 8, 7, 4, 70, 60, 50]
k = 4
print(arr)
insertion_sort_solution(arr, k)
print(arr)

from heapq import heappop, heappush, heapify


def heap_sort_naive(arr, k):
    """
    nlog(n)

    """
    result = []
    heapify(arr)  # This is log(n) operation

    while arr:
        result.append(heappop(arr))

    return result


def heap_sort_smart(arr, k):
    """
    It's nifty because we keep the heapsize only k so we're able to make the entire
    algorithm O(nlog(k))

    """
    result = []

    heap = arr[:k + 1]
    heapify(heap)  # log k operation

    """
    the below operation is nlog(k)
    - The loop goes over O(n) elements
    - heappop() takes log k since the heap is size k
    - heappush() takes log k since the heap is size k
    """
    for remaining_ele_idx in range(k + 1, len(arr)):
        result.append(heappop(heap))
        heappush(heap, arr[remaining_ele_idx])

    while heap:
        result.append(heappop(heap))

    return result


print("heap sort solution")
arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
print(arr)
result = heap_sort_smart(arr, k)
print(result)

print()

arr = [10, 9, 8, 7, 4, 70, 60, 50]
k = 4
print(arr)
result = heap_sort_smart(arr, k)
print(result)
