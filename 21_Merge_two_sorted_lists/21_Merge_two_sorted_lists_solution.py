# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        current_node = res

        while list1 is not None or list2 is not None:

            if list2 is not None and (list1 is None or list1.val > list2.val or list1.val == list2.val):
                current_node.next = ListNode(list2.val)
                list2 = list2.next

            elif list1 is not None and (list2 is None or list1.val < list2.val):
                current_node.next = ListNode(list1.val)
                list1 = list1.next

            current_node = current_node.next

        res = res.next

        return res
