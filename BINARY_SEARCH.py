"""
    THIS MODULE IS CREATED TO IMPLEMENT
    BINARY SEARCH IN A RECURSIVE MANNER

        - USES BINARY SEARCH TO FIND AN ELEMENT

    THE FUNCTIONS IN THIS MODULE ARE ALL
    BASED ON RECURSIVITY.
"""

"""
    AN IMPLEMENTATION OF BINARY SEARCH
"""

def findLargest(arr):
    """
        A RECURSIVE FUNCTION TO FIND 
        LARGEST NUMBER FROM AN ARRAY
    """
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_arr = findLargest(arr[1:])
    return arr[0] if arr[0] > sub_arr else sub_arr

# This is an incomplete function
def sortByLargest(arr):
    """
        SORT AN ARRAY
        FROM LARGEST TO SMALLEST
    """
    if arr == []:
        return
    else:
        newArray = arr.pop()

# binary search recursive function
def binarySearch(arr, f_num):
    """
        A RECURSIVE FUNCTION TO 
        IMPLEMENT BINARY SEARCH TECHNIQUE
        TO FIND AN ELEMENT.
    """
    if len(arr) == 1:
        return 'found' if arr[0] == f_num else 'not found'
    low = 0
    high = len(arr)
    mid = int((low + high) / 2)
    if arr[mid] < f_num:
        return binarySearch(arr[mid:], f_num)
    elif arr[mid] > f_num:
        return binarySearch(arr[:mid], f_num)
    else:
        return 'found'


# Testing Functions
print(findLargest([3,6,4,1,7,5]))
print(binarySearch([2,3,7,9,14,18,26,38,], 26))
