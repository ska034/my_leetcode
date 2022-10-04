# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = {}
        for i in range(lowLimit, highLimit + 1):
            if i > 9:
                box = sum(map(int, str(i)))
            else:
                box = i
            if box not in d:
                d[box] = 1
            else:
                d[box] += 1

        return max(d.values())
