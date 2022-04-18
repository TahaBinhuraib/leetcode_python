"""
Given an integer array nums, return true if any value appears
at least twice in the array, and return false if every element 
is distinct 
"""


def contains_duplicates(nums: list[int]) -> bool:
    logged = {}
    for num in nums:
        if num in logged:
            return True
        logged[num] = 1
    return False


nums = [1, 13, 3, 4, 5, 6, 10, 1]
print(contains_duplicates(nums))
