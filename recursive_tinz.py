"""
    THIS IS A MODULE FOR IMPLEMENTING ALGORITHMS
    DIFFERENT RECURSIVE ALGORITHM IMPLEMENTATIONS
    PRESENT HERE ARE LISTED BELOW:

        - countDown Function
        - sum Function
        - countItem Function
        - findLargest Function
"""

def countDown(num):
    """
        A RECURSIVE FUNCTION TO PRINT COUNTDOWN
        OF A NUMBER PASSED IN.
    """
    if num <= 0:# Base Case
        print(0)
        return
    else:
        print(num, end=", ")
        countDown(num-1) # Recursive Case

def sum(values):
    """
        A FUNCTION TO GET THE SUM OF ALL ELEMENTS
        IN A LIST USING RECURSION
    """
    if values == []:
        return 0
    return values[0] + sum(values[1:])

def countItem(items):
    """
        A RECURSIVE FUNCTION
        TO COUNT THE NUMBER OF ITEMS IN A LIST
    """
    if items == []:
        return 0
    return 1 + countItem(items[1:])

def findLargest(arr):
    """
        A RECURSIVE FUNCTION TO FIND 
        LARGEST NUMBER FROM AN ARRAY
    """
    if len(arr) == 1:
        return arr[0]

    if arr[0] < arr[1]:
        arr.pop(0)
        return findLargest(arr)
    else:
        arr.pop(1)
        return findLargest(arr)


# Using the functions
countDown(50)
print('-' * 10)
print(sum([4,6,3,8,5,8,2,4,5,8]))
print('+'*10)
print(countItem([5,6,4,3,6,9,5,7,2,4,56,4,3]))
print()
print(findLargest([4,6,4,7,2,3,8,9,10,456]))
