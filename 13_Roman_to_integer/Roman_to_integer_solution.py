# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        prev_val, res = 0, 0
        for val in list(s):
            if prev_val != 0 and prev_val < dict[val]:
                res = res + dict[val] - 2 * prev_val
            else:
                res =res + dict[val]
            prev_val = dict[val]

        return res
