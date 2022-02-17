# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root):
        self.answer = float('inf')
        self.min_ = root.val

        def dfs(node):
            if node:
                if node.val == self.min_:
                    dfs(node.left); dfs(node.right)
                elif self.min_ < node.val < self.answer:
                    self.answer = node.val
        dfs(root)
        return self.answer if self.answer != float('inf') else -1
