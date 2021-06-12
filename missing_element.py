"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""




array=[1,5,4,-3,7,-2]   #output=2

def positive_array(array):
    pos_array=[a for a in array if a >= 0 ]
    return pos_array

def missing_element(array):
    temp=positive_array(array)
    temp.sort()
    for num in temp:
        if num+1 in temp:
            continue
        else:
            return num+1
print(missing_element(array))


