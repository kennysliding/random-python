import itertools
from typing import List, Tuple

def bubble_sort(sorting: List) -> Tuple[List, int]:
    """
    A simple bubble sort algorithm that returns the 
    sorted list along with the number of swaps performed

    Parameters:
    sorting (List): the list to sort

    Returns: Tuple[List, int]
    1st (List): the sorted list
    2nd (int): the number of swaps performed
    """  
    count = 0 # count for swapping element
    for i in range(len(sorting) - 1):
        for j in range(len(sorting) - 1):
             if sorting[j] > sorting[j + 1]:
                 temp = sorting[j]
                 sorting[j] = sorting[j + 1]
                 sorting[j + 1] = temp
                 count += 1
    return sorting, count

# to test the function
for n in range(10):
    test_input = [x for x in range(n)]
    sum = 0
    a = 0
    for subset in itertools.permutations(test_input, n):
        _, count = bubble_sort(list(subset))
        sum += count
        a += 1
    print(n, sum / a)