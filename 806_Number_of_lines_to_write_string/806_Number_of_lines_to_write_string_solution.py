# https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 0
        number = 1
        length = len(s)

        if s is None:
            return []

        for i in range(length):
            line += widths[ord(s[i]) - 97]
            if line > 100:
                line = widths[ord(s[i]) - 97]
                number += 1

        return [number, line]
