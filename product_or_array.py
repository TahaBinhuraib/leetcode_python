"""
Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i]
input = [1, 2, 3, 4]
output = [24, 12, 8, 6]
"""


def product_of_array_except_self(nums: list[int]) -> list[int]:
    returned = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        returned[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        returned[i] = postfix * returned[i]
        postfix *= nums[i]

    return returned


print(product_of_array_except_self([1, 2, 3, 4]))
