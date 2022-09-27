# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        res = 0
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d.pop(i)
                res += 2
        if d.keys():
            res += 1
        return res
