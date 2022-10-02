# https://leetcode.com/problems/count-prefixes-of-a-given-string/description/

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for i in words:
            if i == s[:len(i)]:
                res += 1
        return res
