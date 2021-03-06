'''
Custom Python implementation
of Sorting Algorithms found in
The Algorithm Design Manual
by Steven S. Skiena

Author: Tomjo Soptame
Date: 6/17/2014
Last Modified: 6/18/2014
'''


# Insertion Sort Algorithm
def insertion_sort(lst):
    print lst
    if type(lst) is str:  # Check to see if the arg type is a string
        lst = [l for l in lst]
    i = 0  # Initial counter to iterate through list
    n = len(lst)  # The upper limit of the list
    while i < n:
        j = i  # Second counter to help keep track of current and current -1
        while j > 0 and lst[j] < lst[j-1]:
            # Sorting/swapping logic
            # Basically if current < previous
            # swap their order.
            cpy = lst[j]
            cpy_1 = lst[j-1]
            lst[j] = cpy_1
            lst[j-1] = cpy
            j -= 1
        i += 1
    return lst


# Selection Sort Algorithm
def selection_sort(lst):
    print lst
    if type(lst) is str:
        lst = [l for l in lst]
    sort_lst = []
    while len(lst) > 0:
        sort_lst.append(min(lst))
        lst.pop(lst.index(min(lst)))
    return sort_lst


# Merge Sort Algorithm
def merge_sort(lst, low=None, high=None):
    print lst
    if type(lst) is str:
        lst = [l for l in lst]
    new_lst = []

    # Essentially we want to sort out the halves
    # Probably implement some form of the swap logic
    # used in insertion_sort.
    def merge(lst, low, middle, high):
        pass

    if not low and not high:
        low = 0
        high = len(lst)

    if low < high:
        middle = (low + high) / 2
        mergesort(lst, low, middle)
        mergesort(lst, middle+1, high)
        merge(lst, low, middle, high)

    return new_lst


# The main function
# to run the program
def main():
    print insertion_sort("INSERTIONSORT")
    print selection_sort("SELECTIONSORT")
    print merge_sort("MERGESORT")

# Only run the program if we're in the
# if it's not being imported as a module.
if __name__ == '__main__':
    main()
