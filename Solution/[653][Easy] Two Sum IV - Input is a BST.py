# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k):
        stack, vals = [root], set()
        while stack:
            node = stack.pop()
            if k-node.val in vals: return True
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            vals.add(node.val)
        return False
