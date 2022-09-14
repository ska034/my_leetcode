# https://leetcode.com/problems/super-pow/

class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        for i in range(len(b)):
            b[i] = str(b[i])
        b = "".join(b)
        return pow(a,int(b),1337)
