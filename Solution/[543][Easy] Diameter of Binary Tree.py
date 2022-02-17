# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        answer, _, _ = self.recursion(root)
        return answer

    def recursion(self, node):
        if node:
            total_l, left_l, right_l = self.recursion(node.left)
            total_r, left_r, right_r = self.recursion(node.right)
            left, right = 1 + max(left_l, right_l), 1 + max(left_r, right_r)
            total = max(total_l, total_r, left+right)
            return total, left, right
        return -1, -1, -1
