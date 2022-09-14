# https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums = [1,2,1]
        new_nums = []
        for i in range(len(nums)):
            new_nums.insert(i,nums[i])
            new_nums.insert(i+len(nums), nums[i])

        return new_nums
