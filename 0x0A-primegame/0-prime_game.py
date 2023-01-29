#!/usr/bin/python3
"""Prime number game"""


def isWinner(x, nums):
    """Function that performs prime game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    tcase = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not tcase[i]:
            continue
        for j in range(i * i, n + 1, i):
            tcase[j] = False
    tcase[0] = tcase[1] = False
    c = 0
    for i in range(len(tcase)):
        if tcase[i]:
            c += 1
        tcase[i] = c
    player1 = 0
    for n in nums:
        player1 += tcase[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
