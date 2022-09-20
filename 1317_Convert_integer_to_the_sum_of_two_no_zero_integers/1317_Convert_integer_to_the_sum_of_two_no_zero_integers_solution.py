# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if "0" not in str(i):
                j = n - i
                if "0" not in str(j):
                    return [i, j]
