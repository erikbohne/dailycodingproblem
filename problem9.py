"""
april 28th 2023

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
from time import sleep

def scheduler(function, ms):
    sleep(1e-3 * ms)
    function()
    
def test():
    print("hello, world!")
    
scheduler(test, 3000)
