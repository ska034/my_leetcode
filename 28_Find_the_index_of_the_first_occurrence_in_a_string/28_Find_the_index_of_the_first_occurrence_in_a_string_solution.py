# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ln_n = len(needle)
        ln_h = len(haystack) - ln_n
        i = 0
        while i <= ln_h:
            if haystack[i:i+ln_n] == needle:
                return i
            else:
                    i += 1
        return -1
