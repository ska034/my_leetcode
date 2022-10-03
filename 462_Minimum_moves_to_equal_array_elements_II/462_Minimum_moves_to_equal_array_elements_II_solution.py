# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ln = len(nums)
        middle = ln // 2
        res = 0

        for i in range(ln):
            res = res + abs(nums[i] - nums[middle])
        return res
