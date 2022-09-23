# https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)

        res = nums[-3] * nums[-2] * nums[-1]
        res2 = nums[0] * nums[1] * nums[-1]

        if res > res2:
            return res
        else:
            return res2
