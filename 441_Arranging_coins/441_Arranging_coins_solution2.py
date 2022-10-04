# https://leetcode.com/problems/arranging-coins/description/
from math import sqrt

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(sqrt(2 * n + 0.25) - 0.50)
