#!/usr/bin/python3
"""
Module to determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened.
    """
    box = 0
    openBox = 0
    keys = []
    keys = keys + boxes[0]
    boxes.pop(0)
    eys = []
    closedBox = {}
    for column in boxes:
        box = box + 1
        
        if box in keys:
            openBox = openBox + 1
            keys = keys + column
        else:
            closedBox[box] = column
            eys.append(box)
        for shutBox in eys:
            if shutBox in keys and shutBox != 0:
                keys = keys + closedBox[shutBox]
                openBox = openBox + 1
                eys.remove(shutBox)
    if openBox == box:
        return True
    return False

    