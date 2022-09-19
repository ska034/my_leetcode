# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        current_node = res
        if head != None and head.val == 0:
            current_node.next = ListNode(0)
            current_node = current_node.next
        while head is not None:
            if current_node.val == head.val:
                head = head.next
            else:
                current_node.next = ListNode(head.val)
                current_node = current_node.next
                head = head.next
        res = res.next

        return res
