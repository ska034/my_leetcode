# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        str_num = str(num)
        length = len(str_num)
        for i in range(length):
            if len(str_num[i:i + k]) == k and int(str_num[i:i + k]) != 0:
                if num % int(str_num[i:i + k]) == 0:
                    res += 1
        return res
