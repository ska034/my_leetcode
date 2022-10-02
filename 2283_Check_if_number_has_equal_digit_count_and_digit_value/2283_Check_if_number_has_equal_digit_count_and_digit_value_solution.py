# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/
from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        print(c)
        for i, x in enumerate(num):
            if c[str(i)] != int(x):
                return False
        return True
