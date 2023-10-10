def num_of_adds(n):
    """ Returns the number of adds used by the recursive 
    fibonacci calculation function for a given n.
    Note: this is simply the recurrence relation for
    the number of adds, written in python.
    """
    if n <= 2:
        return 0  
    else:
        return num_of_adds(n-1)+num_of_adds(n-2)+1
print(num_of_adds(7))