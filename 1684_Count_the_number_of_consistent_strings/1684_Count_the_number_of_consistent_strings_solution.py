# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        set_allowed = set(allowed)
        for word in words:
            set_word = set(word)
            if set_allowed == set_word or set_word <= set_allowed:
                res += 1
        return res
