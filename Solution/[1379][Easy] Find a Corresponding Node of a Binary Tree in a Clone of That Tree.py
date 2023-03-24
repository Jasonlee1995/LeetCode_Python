# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        val = target.val
        stack = [cloned]
        while stack:
            temp = []
            for node in stack:
                if node.val == val:
                    return node
                else:
                    if node.left: stack.append(node.left)
                    if node.right: stack.append(node.right)
            stack = temp