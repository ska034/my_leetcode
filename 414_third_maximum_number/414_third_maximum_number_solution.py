# https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        if len(nums) > 2:
            return nums[2]
        else:
            return nums[0]
