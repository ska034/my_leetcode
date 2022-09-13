# https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        new_nums = []
        for i in nums:
            new_nums.append(set(i))

        return sorted(list(set.intersection(*new_nums)))
