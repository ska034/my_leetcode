# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for symbol in s:
            if symbol in ['(', '[', '{']:
                res.append(symbol)
            elif symbol == ')' and len(res) != 0 and res[-1]=='(':
                res.pop()
            elif symbol == ']' and len(res) != 0 and res[-1]=='[':
                res.pop()
            elif symbol == '}' and len(res) != 0 and res[-1]=='{':
                res.pop()
            else:
                return False
        if res == []:
            return True
