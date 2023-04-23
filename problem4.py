"""
april 23rd 2023

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
    
Implement car and cdr.
"""
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def first(a, _):
        return a
    return pair(first)

def cdr(pair):
    def last(_, b):
        return b
    return pair(last)

print(f"car(cons(3, 4)) -> {car(cons(3, 4))}")
print(f"cdr(cons(3, 4)) -> {cdr(cons(3, 4))}")