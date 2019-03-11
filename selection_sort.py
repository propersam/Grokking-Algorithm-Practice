
def findSmallest(arr):
    """
        Fucntion to find smallest element from array
        and return it's index location

        >> findSmallest([4,7,1,9,6,0])
        2
    """
    smallest = arr[0] # assign the element in array as smallest
    smallest_index = 0 # assign first index of array as index with smallest value

    for i in range(1,len(arr)):# loop through the array_list
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):

    """
        Function to Sort an array
        from smallest to Largest

        >> selectionSort([5,7,4,2,3,1,9,0])
        [0,1,2,3,4,5,7,9]
    """

    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10, 78, 0]))

