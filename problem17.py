"""
may 6th 2023

This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. 
You can modify the input array in-place and you do not need to store the results. 
You can simply print them out as you compute them.
"""
def max_values(array: list, k: int):
    for i in range(len(array)):
        if k + i <= len(array):
            print(max([array[i] for i in range(i, i + k)]))

array1 = [10, 5, 2, 7, 8, 7]
k1 = 3
max_values(array1, k1)

array2 = [2, 3, 4, 7, 6, 4, 1]
k2 = 5
max_values(array2, k2)
