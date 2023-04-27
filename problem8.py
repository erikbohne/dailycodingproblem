"""
27th april 2023

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
import numpy as np

def largest_sum(array):
    SUM = 0
    array = np.array(array, dtype = float)
    for _ in array:
        idx = array.argmax()
        if idx == len(array) - 1: # Handle if idx is the last in the array
            if array[idx - 1] == np.NINF:
                array[idx] = np.NINF
                continue
            else:
                SUM += array[idx]
                array[idx] = np.NINF
                continue
            
        if idx == 0: # Handle if idx is the first in the array
            if array[idx] == np.NINF:
                array[idx] = np.NINF
                continue
            else:
                SUM += array[idx]
                array[idx] = np.NINF
                continue
            
        if array[idx + 1] > np.NINF and array[idx - 1] > np.NINF:
            SUM += array[idx]
            array[idx] = np.NINF
        else:
            array[idx] = np.NINF + 1
            
    return int(SUM)

array1 = [2, 4, 6, 2, 5]
print(largest_sum(array1))

array2 = [5, 1, 1, 5]
print(largest_sum(array2))
