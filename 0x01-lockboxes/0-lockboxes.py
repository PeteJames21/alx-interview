#!/usr/bin/env python3
"""
An implementation of the lockboxes algorithm.
"""
from typing import List, Set


def canUnlockAll(boxes: List[List[int]]):
    """Return True if all boxes can be unlocked, else False."""
    # print('boxes:', boxes)
    # print('--------------')

    if not boxes:
        return True

    # Open the first box and mark it as opened by setting index value to None
    keys = set()
    keys.update(boxes[0])
    boxes[0] = None

    while True:
        try:
            # print('keys:', keys)
            # print('boxes:', boxes)
            # print('--------------')

            # Open a box and retrieve the keys
            # The key used to open the box will be removed from the set of keys
            key = keys.pop()
            if boxes[key]:
                keys.update(boxes[key])
            # Mark a box as opened
            boxes[key] = None
        except IndexError:
            # Key does not open any box
            pass
        except KeyError:
            # No more keys
            # Returns True if all boxes are opened.
            # print('No more keys')
            return not any(boxes)
