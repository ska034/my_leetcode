class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        sum = 0
        for i in range(len(nums)):
            if i == 0:
                sum += nums[i]
            else:
                if nums[i] <= nums[i - 1]:
                    if sum > res:
                        res = sum
                    sum = nums[i]
                else:
                    sum += nums[i]
        if sum > res:
            res = sum

        return res
