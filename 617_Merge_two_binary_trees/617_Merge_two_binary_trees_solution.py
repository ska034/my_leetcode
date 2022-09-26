# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec_func(node1, node2):
            if node1 and node2:
                new_root = TreeNode(node1.val + node2.val)
                new_root.left = rec_func(node1.left, node2.left)
                new_root.right = rec_func(node1.right, node2.right)

                return new_root
            else:
                return node1 or node2

        return rec_func(root1, root2)
