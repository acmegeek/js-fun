#! /usr/bin/env python3
# -------------------------------- #
# File name: find_consecutive_runs.py
# Author: Sam Douglas
# Date created: 07/05/2016
# Date last modified: 07/05/2016
# Python Version: 3.5.2
# -------------------------------- #
#


def find_consecutive_runs(integer_list):
    runs = []
    list_length = len(integer_list)

    for i, n in enumerate(integer_list):
        if (i < list_length - 2):
            n1 = integer_list[i + 1]
            n2 = integer_list[i + 2]

            # Make sure all 3 items are integers
            if (type(n) is int and type(n1) is int and type(n2) is int):
                # Ensure that the 3 are a ascending or descending series
                if ((n2 > n1 and n1 > n) or (n2 < n1 and n1 < n)):
                    # Test for the increase or decrease by 1 run criteria
                    if (abs(n2 - n) == 2 and abs(n1 - n) == 1):
                        # if all conditions met, add run start index to list
                        runs.append(i)
    if (len(runs) == 0):
        runs = 'None'
    return runs  # return runs found or None

print('test Example')
print(find_consecutive_runs([1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]))

print('test Example with changed integer')
print(find_consecutive_runs([1, 2, 3, 5, 10, 11, 8, 9, 10, 11, 7, 8, 7]))

print('test Example with decimal')
print(find_consecutive_runs([1, 2, 3, 5, 10.5, 9, 8, 9, 10, 11, 7, 8, 7]))

print('test Example with strings')
print(find_consecutive_runs([1, '2', 3, 5, '10', 9, 8, 9, 10, '11', 7, 8, 7]))

print('test Example with object')
print(find_consecutive_runs([1, 2, 5, {'foo': 5}, 9, 8, 9, 10, 11, 7, 8, 7]))

print('test repeated')
print(find_consecutive_runs([1, 1, 1, 1, 1, 1, 2, 3, 2, 1]))

print('test negative numbers')
print(find_consecutive_runs([-1, -2, -3, -2, -1, 0, 1, 2]))

print('test no matches')
print(find_consecutive_runs([7, 3, 56, 74, 3, 1, 1]))

print('test long run')
print(find_consecutive_runs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

print('test with larger and more random numbers')
print(find_consecutive_runs([34, 35, 36, 6, 423, 4, 45, 5, 5, 6455, 456,
 3, 456, 457, 458, 876543, 876542, 876541, 11, 7, 8, 6, 2345624562456245,
 2345624562456246, 2345624562456247]))
