def linear_search(arr, target):
    # in case of empty array
    if len(arr) is None:
        return -1
    # checks to see if the index is equal to what we want
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # set up variables to change
    low = 0
    # high is total len of arr
    high = len(arr) - 1
    mid = 0

    while low <= high:
        # to get middle of arr whule still being able to change where the middle is
        mid = (high + low)
        # If x is greater, ignore left half
        if arr[mid] < target:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > target:
            high = mid - 1
        # else, x is present at mid
        else:
            return mid
        # works since we know the array is sorted
    return -1  # not found
