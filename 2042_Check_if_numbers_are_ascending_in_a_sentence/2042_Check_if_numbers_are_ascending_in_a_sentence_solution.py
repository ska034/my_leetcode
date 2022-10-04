# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        number = -1
        s = s.split()
        for i in s:
            if i.isdigit():
                if int(number) < int(i):
                    number = i
                else:
                    return False
        return True
