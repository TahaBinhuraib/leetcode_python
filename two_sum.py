"""
Given an array of integers, return indeces of the two 
numbers such that they sum up to a specific target
[2, 7, 11, 5] -> target = 9
return -> [0, 1]
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    hash_map = {}  # val : index
    for index, value in enumerate(nums):
        diff = target - value
        if diff in hash_map:
            return [hash_map[diff], index]
        hash_map[value] = index


l_of_numbers = [1, 3, 5, 7]
target = 4

print(two_sum(nums=l_of_numbers, target=target))
