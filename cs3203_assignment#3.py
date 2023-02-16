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

def arrayProduct(arr):
    count = 1
    for i in arr:
        count *= i
    return count

print(arrayProduct(arr))

def arrayReverse(arr):
    arr.reverse()
    return arr

print(arrayReverse(arr))

### Main Program ###
if __name__ == "__main__":
    
    inputArr = []
    
    size = int(input("Enter the desired size of the array: "))
    
    for i in range(0, size):
        elements = int(input("Enter an element: "))
        inputArr.append(elements)
        
    print("The sum of all elements in the array = " + str(arraySum(inputArr)))
    print("The product of all elements in the array = " + str(arrayProduct(inputArr)))
    print("The array in reverse order = " + str(arrayReverse(inputArr)))
### End Main Program ###