# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = ""
        while head is not None:
            number = number + str(head.val)
            head = head.next
        length = len(number)
        res = 0
        for i in range(length):
            res = res + int(number[i]) * (2**(length-i-1))

        return res
