# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode()
        current_node = res
        while head != None:
            if head.val != val:
                current_node.next = ListNode(head.val)
                current_node = current_node.next
                head = head.next
            else:
                head = head.next
        res = res.next

        return res
