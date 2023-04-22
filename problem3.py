"""
april 22th 2023

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def missing_integer(array):
    for i in range(1, len(array) + 1):
        if i not in array:
            return i

for test in [[3, 4, -1, 1], [1, 2, 0]]:
    print(f"{test} -> {missing_integer(test)}")