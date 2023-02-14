# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:28:30 2023

@author: James
"""

def arraySum(arr):
    count = 0
    for i in arr:
        count += i
    return count

arr = [8, 26, 14, 5, 32]
print(arraySum(arr))