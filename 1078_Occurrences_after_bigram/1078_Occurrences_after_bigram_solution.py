# https://leetcode.com/problems/occurrences-after-bigram/description/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(" ")
        ln = len(text)
        res = []
        i = 0
        while i < ln:
            if text[i] == first:
                if i < ln-2 and text[i+1] == second:
                    res.append(text[i+2])
            i += 1

        return res
