# https://leetcode.com/problems/percentage-of-letter-in-string/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        ln = 0
        for i in s:
            if i == letter:
                count += 1
            ln += 1
        return count * 100 // ln
