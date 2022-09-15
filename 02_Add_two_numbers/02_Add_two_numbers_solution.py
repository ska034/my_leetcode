# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        digit, val_l1, val_l2 = 0, 0, 0
        res = ListNode()
        current_node = res
        while l1 is not None or l2 is not None:
            if l1 is not None:
                val_l1 = l1.val
                l1 = l1.next
            else:
                val_l1 = 0

            if l2 is not None:
                val_l2 = l2.val
                l2 = l2.next
            else:
                val_l2 = 0

            sum = val_l1 + val_l2 + digit
            digit = sum // 10

            current_node.next = ListNode(sum % 10)
            current_node = current_node.next

        if digit > 0:
            current_node.next = ListNode(digit)

        res = res.next
        return res
