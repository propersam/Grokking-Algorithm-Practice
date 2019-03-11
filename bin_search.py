def binary_search(lis, item):
    """ 
        A FUNCTION TO IMPLEMENT BINARY-SEARCH TO 
        SEARCH THROUGH A LIST/ARRAY AND FIND AN ELEMENT
    """
    low = 0 # Setting the index location of the lower bound
    high = len(lis) - 1 # Setting the index location of the upper bound 
    
    # Using while control structure to loop through the list
    while low <= high: # A long as we have not reached the end of the list

        mid = int((low + high) / 2) # Getting and Setting index of the Mid point
        guess = lis[mid] # Store the Mid Value 

        # Check if value acquired value is what we are looking for
        # Perform necessary action
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list =[1,2,3,4,5,6,7,8]
print(binary_search(my_list, 2))
print(binary_search(my_list, 6))
print(binary_search(my_list, 20))
