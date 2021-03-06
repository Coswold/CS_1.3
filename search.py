#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index > len(array) - 1:
        return None
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    middle = len(array) // 2
    left = 0
    right = len(array) - 1
    while right >= left:
        if array[middle] == item:
            return middle
        elif item > array[middle]:
            left += 1
            middle += (len(array) - middle) // 2
        else:
            right = middle - 1
            middle //= 2
    return None


def binary_search_recursive(array, item, left=None, right=None):
    if left == None and right == None:
        left = 0
        right = len(array) - 1
    i = (left + right) // 2
    if array[i] == item:
        return i
    if left > right:
        return None
    elif item < array[i]:
        right = i - 1
        return binary_search_recursive(array, item, left, right)
    else:
        left = i + 1
        return binary_search_recursive(array, item, left, right)


names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
print(binary_search(names, 'Jeremy'))
