# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index_one = i
            for j in range(i + 1, len(nums)):
                index_two = j
                if nums[i] + nums[j] == target and index_one != index_two:
                    output = [index_one, index_two]
                    return output



