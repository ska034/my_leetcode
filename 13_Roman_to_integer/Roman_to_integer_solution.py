# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        res = []


        # if num // 1 > 0:
        #     if num // 1 == 4:
        #         res.append("IV")
        #     else:
        #         res.append(num // 1 * "I")

        return res


print(Solution().intToRoman(19))
