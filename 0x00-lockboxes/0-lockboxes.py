#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Function that checks with boolean value if the list type and
    length to invoke two for iterations one to traverse the list
    and the other to compaer if key is idx or not in order to open
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
