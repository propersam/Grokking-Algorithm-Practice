def factorial(num):
    """
        A RECURSIVE FUNCTION 
        TO GET THE FACTORIAL OF 'num'
    """

    if num == 1: # Base Case
        return 1
    else: # Recursive Case
        return num * factorial(num-1)


print(factorial(20))
