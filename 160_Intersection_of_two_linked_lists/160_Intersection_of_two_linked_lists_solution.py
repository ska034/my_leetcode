# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dictA = {}
        while headA is not None:
            dictA[headA] = headA.val
            headA = headA.next
        while headB is not None:
            if headB in dictA:
                return headB
            else:
                headB = headB.next
        return None
