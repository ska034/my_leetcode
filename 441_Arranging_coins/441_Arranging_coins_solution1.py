# https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        floor = 1
        while n >= 0:
            n = n - floor
            if n >= 0:
                res += 1
            floor += 1
        return res
