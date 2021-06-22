"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]. 
How many different ways do you know to solve this problem?
"""
from collections import deque

def rotate_array(arr: list = None, offset: int = None):
    return deque(arr).rotate(offset)
