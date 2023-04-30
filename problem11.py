"""
april 30th 2023

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, 
you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
def ways_to_climb(n_steps, stair):
    ways = {0: 1}
    for step in range(1, stair + 1):
        ways[step] = 0
        for steps in n_steps:
            if step - steps >= 0:
                ways[step] += ways[step - steps]
    
    return ways[step]

print(ways_to_climb([1, 2], 4))

print(ways_to_climb([1, 3, 5], 4))
    
    
