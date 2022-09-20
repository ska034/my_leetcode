# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        sum = 0
        for score in operations:
            if score == "+":
                res.append(int(res[-1]) + int(res[-2]))
            elif score == "C":
                res.pop()
            elif score == "D":
                res.append(res[-1] * 2)
            else:
                res.append(int(score))

        for new_score in res:
            sum += new_score

        return sum
