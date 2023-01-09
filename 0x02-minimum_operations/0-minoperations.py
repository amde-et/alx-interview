#!/usr/bin/python3

"""
   In a text file, there is a single character H. Your text editor
   can execute only two operations in this file: Copy All and Paste.
   Given a number n, write a method that calculates the fewest
   number of operations needed to result in
   exactly n H characters in the file.
"""


def minOperations(n):
    num_ops = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            num_ops += min_ops
            n /= min_ops
        min_ops += 1
    return num_ops
