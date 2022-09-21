# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
                if d[i] == 2:
                    return True
            else:
                d[i] = 1

        return False
