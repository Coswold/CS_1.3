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
    # TODO: implement linear search recursively here
    if index > len(array) - 1:
        return None
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    i = len(array) // 2
    left = 0
    right = len(array) - 1
    while right >= left:
        if array[i] == item:
            return i
        elif item > array[i]:
            left = i + 1
            i = i + (len(array) - i) // 2
        else:
            right = i - 1
            i = i // 2
    return None


    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left == None and right == None:
        left = 0
        right = len(array) - 1
    i = (left + right) // 2
    print(left, right, i)
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

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
print(binary_search(names, 'Jeremy'))
