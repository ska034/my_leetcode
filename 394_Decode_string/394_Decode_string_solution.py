# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        for char in s:
            if char != "]":
                res.append(char)
            else:
                str = ""
                while res and res[-1] != "[":
                    str = res.pop() + str
                if res:
                    res.pop()
                    amount = ""
                    while res and res[-1].isdigit():
                        amount = res.pop() + amount
                    res.append(int(amount) * str)

        return "".join(res)
