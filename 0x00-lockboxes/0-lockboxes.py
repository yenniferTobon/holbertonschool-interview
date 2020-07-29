#!/usr/bin/python3

def canUnlockAll(boxes):
    box = 0
    openBox = 0
    keys = []
    closedBox = 0
    keys = keys + boxes[0]
    boxes.pop(0)
    lockedKeys = []
    for column in boxes:
        box = box + 1
        if closedBox in keys and closedBox != 0:
            keys = keys + lockedKeys
            openBox = openBox + 1
            closedBox = 0
        if box in keys:
            openBox = openBox + 1
            keys = keys + column
        else: 
            closedBox = box
            lockedKeys = column
    if openBox == box:
        return True
    return False



