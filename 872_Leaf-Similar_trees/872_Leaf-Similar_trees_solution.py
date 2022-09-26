# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def rec_func(node, res):
            if not node:
                return res
            if not node.left and not node.right:
                return res.append(node.val)
            rec_func(node.left, res)
            rec_func(node.right, res)

        res1 = []
        res2 = []
        rec_func(root1, res1)
        rec_func(root2, res2)

        return res1 == res2
