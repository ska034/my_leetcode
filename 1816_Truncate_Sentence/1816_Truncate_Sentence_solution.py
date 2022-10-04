# https://leetcode.com/problems/truncate-sentence/description/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])

# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         res = ""
#         for i in s:
#             if i == " ":
#                 k -= 1
#             if k == 0:
#                 return res
#             res += i
#         return res
