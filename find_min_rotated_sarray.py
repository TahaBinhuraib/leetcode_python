"""
Suppose an array of length n sorted in ascending order is rotated
between 1 and n times. For example, the array 
[0, 1, 2, 3, 4, 5, 6, 7]
might become:
[4, 5, 6, 7, 0, 1, 2] if rotated 4 times
[0, 1, 2, 3, 4, 5, 6, 7] if rotated 7 times

Example:
input = [3, 4, 5, 1, 2]
output = 1
Explanation: the original array was [1, 2, 3, 4, 5] rotated 3 times.
Solve in O(logn) time
Every value in the list is unique!
"""
# We will use the binary search algorithm that runs in O(logn) time!


def solve(nums: list[int]) -> int:
    res = nums[0]
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break
        m = (left + right) // 2
        res = min(res, nums[m])
        if nums[m] > nums[left]:
            left = m + 1
        else:
            right = m - 1

    return res


nums = [3, 4, 5, 1, 2]
print(solve(nums=nums))
