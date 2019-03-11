# ALGORITHM IMPLEMENTATIOIN FOR QUICK SORT
import time

def quick_sort(arr):
    
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left_side = [i for i in arr[1:] if i <= pivot]
    right_side = [i for i in arr[1:] if i > pivot ]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


# Testing the Quick Sort
time_start = time.time()
print(quick_sort([4,7,3,6,2,7,5,9]))
sort_time = time.time() - time_start
print("This algorithm ran in " + str(sort_time) + "s. ")
