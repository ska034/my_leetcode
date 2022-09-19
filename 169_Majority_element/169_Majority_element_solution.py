# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        new_dict = {}
        for i in nums:
            if i in new_dict:
                new_dict[i] = new_dict[i] + 1
            else:
                new_dict[i] = 1
        return max(new_dict.keys(), key=new_dict.get)
