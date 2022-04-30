"""
Given an unsorted list of ints, find the length of the longes consecutive elements sequence
Should run in O(n)
input = [100, 4, 200, 1, 2, 3]
output = 4
explanation: the longest consecutive elements sequence is [1, 2, 3, 4]. Which has a length of 4
"""
# We first determine the starts of sequence. A number would be a start of a sequence if number - 1 does not
# exist! Then we find the length of the sequence by checking if number + 1 exists and so on...


def solve(nums: list[int]) -> int:
    uniques = list(set(nums))
    longest = 0
    for i in nums:
        if (i - 1) not in uniques:
            length = 0
            while (i + length) in uniques:
                length += 1
            longest = max(length, longest)

    return longest


input = [100, 4, 200, 1, 2, 3]
print(solve(input))
