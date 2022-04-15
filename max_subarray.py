"""
Given an integer array, find the contiguous subarray which has 
the largest sum and return its sum
"""


def max_subarray(nums: list[int]) -> int:
    max_sub = nums[0]
    current = 0
    for number in nums:
        if current < 0:
            current = 0
        current += number
        max_sub = max(current, max_sub)
    return max_sub


nums = [1, -3, 1, 3, 4, 5, -1, -12, 1, 2, 3, 10]
print(max_subarray(nums=nums))
