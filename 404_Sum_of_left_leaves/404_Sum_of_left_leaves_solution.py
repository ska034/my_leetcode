# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def rec_func(node):
            if not node or not node.left and not node.right:
                return

            if node.left:
                if not node.left.left and not node.left.right:
                    self.res += node.left.val
            rec_func(node.left)
            rec_func(node.right)

        rec_func(root)

        return self.res
