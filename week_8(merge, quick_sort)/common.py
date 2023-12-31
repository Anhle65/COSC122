from quicksort import *


def read_data(filename):
    """ Returns a list of integers read from the file """
    with open(filename) as infile:
        values = [int(line.strip()) for line in infile]
    return values


def common_items(list_x, list_y):
    """ Takes two sorted lists as input (ie, both lists are in ascending order).
    Returns a list containing all the items in list_x that are also in list_y.
    Returns an empty list if there are none.

    The resulting list should be in order and only contain one instance of each
    item that appears in both lists, ie, common items should only be listed once.
    NOTE: You should use a method similar to the merge function in mergesort,
    that is, use a while loop and a couple of indices. Don't use any for loops!

    First write code for dealing with two lists that each contain only uniques values.
    When you have that running, update it so that it deals with lists that don't
    contain all unique values, see the commented doctests below

    NOTES:
    Your function will need to use only one while loop.
    Your function shouldn't use expressions like:
       - item in alist
       - for item in alist

    >>> common_items([0,1,2,3],[1,2,3,4])
    [1, 2, 3]
    >>> common_items([0,1,2,3],[0,1,2,3])
    [0, 1, 2, 3]
    >>> common_items([0,1,2,3],[5,6,7,8])
    []
    >>> common_items([],[5,6,7,8])
    []
    >>> common_items([1,2,3,4],[])
    []
    >>> common_items([],[])
    []
    >>> common_items([0,1,2,3],[0,0,2,4])
    [0, 2]
    >>> common_items([0,1,2,2,5,5,6,6,7,8,8,9,9,9,9],[0,0,2,4,5,5,5,7,8,9])
    [0, 2, 5, 7]
    """
    # add the following doctests (and some of your own)
    # when ready for lists of non-unique items
    # >>> common_items([0,1,2,3],[0,0,2,4])
    # [0, 2]
    # >>> common_items([0,1,2,2,5,5,6,6,7],[0,0,2,4,5,5,5,7])
    # [0, 2, 5, 7]

    # ---start student section---
    common = []
    i = 0
    j = 0
    condition = False
    finish = False
    set1 = set(list_x)
    set2 = set(list_y)
    commonset = set1.intersection(set2)
    # return set1.intersection(set2)
    while i < len(list_x) and not finish:
        if j >= len(list_y):
            condition = True
            if j == i:
                finish = True
            j = 0
        else:
            if j < len(list_y) and not condition:
                if list_x[i] == list_y[j]:
                    common.append(list_x[i])
                j += 1
            else:
                condition = False
                i += 1
    return (set(common))
    # set1 = set(list_x)
    # set2 = set(list_y)
    # return set1.intersection(set2)
    # ===end student section===


if __name__ == "__main__":
    # doctest.testmod()
    print((common_items(read_data("data/ordered_unique_12.txt"), read_data("data/ordered_unique_13.txt"))))