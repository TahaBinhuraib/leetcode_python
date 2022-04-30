"""
Given n non-negative integers, where each represents a point at coordinate (i, ai) n vertical lines 
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which, together with the x-axis forms a container, such that the container contains the most water

Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
output = 49
"""


def brute_force(heights: list[int]) -> int:
    res = 0
    for left in range(len(heights)):
        for right in range(left + 1, len(heights)):
            area = (right - left) * min(heights[left], heights[right])
            res = max(res, area)

    return res


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(brute_force(heights))

# This solution will assume that the maximum contained amount is when
# we have the greatest width; left = 0, right = len(heights)
# We will use a two pointer approach to find the max
# Since the height is the limiting factor, we will shift the side with the shorter width


def linear_time(heights: list[int]) -> int:
    res = 0
    left = 0
    right = len(heights) - 1
    while right > left:
        area = (right - left) * min(heights[left], heights[right])
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

        res = max(res, area)

    return res


print(linear_time(heights=heights))
