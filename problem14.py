"""
may 3rd 2023

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
import random

# Use the Reservoir Sampling algorithm
def pick_random(stream):

    selected_element = None
    count = 0
    
    for element in stream:
        count += 1
        r = random.randint(1, count)
        
        if r == 1:
            selected_element = element
        
    return selected_element

stream = [1, 2, 3, 4, 5, 6, 7]
print(pick_random(stream))