# https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums = [1, 2, 1]
        new_nums = []
        length = len(nums)
        for i in range(length):
            new_nums.insert(i, nums[i])
            new_nums.insert(i + length, nums[i])

        return new_nums
