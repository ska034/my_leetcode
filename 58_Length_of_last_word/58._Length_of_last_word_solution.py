# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.split()
        print(new_s)
        if "!" in new_s[-1] or "." in new_s[-1] or "?" in new_s[-1]:
            return len(new_s[-2])
        else:
            return len(new_s[-1])
