# https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        res = 0
        for i in costs:
            coins = coins - i
            if coins < 0:
                return res
            else:
                res += 1
        return res
