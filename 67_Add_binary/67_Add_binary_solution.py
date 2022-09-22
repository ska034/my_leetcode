# https://leetcode.com/problems/add-binary/submissions/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)
        res = bin(a + b)[2:]

        return res
