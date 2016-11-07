import sys, os

def sum(numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print sum([1, 2, 3])
