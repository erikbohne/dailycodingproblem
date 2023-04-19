"""
april 19th 2023

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def adds_up(list, k):
    # turn the list to a set
    numbers = set(list)

    for number in numbers:
        if k - number != number and k - number in numbers:
            return True
    else:
        return False

list = [10, 15, 3, 7]
k = input("k: ")

if adds_up(list, int(k)):
    print("Solution found")
else:
    print("Solution NOT found")
    