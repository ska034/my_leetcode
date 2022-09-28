# https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        positon = 0
        for i in range(1, n + 1):
            if n % i == 0:
                positon += 1
                if positon == k:
                    return i
        return -1
