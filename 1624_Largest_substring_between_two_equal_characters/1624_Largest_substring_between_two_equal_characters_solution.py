# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        res = 0

        if len(set(s)) == len(s):
            return -1
        else:
            for i, v in enumerate(s):
                if v not in d:
                    d[v] = i
                else:
                    if i - d[v] - 1 > res:
                        res = i - d[v] - 1
            return res
