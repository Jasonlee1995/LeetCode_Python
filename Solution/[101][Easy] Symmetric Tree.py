# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if root == None: return True
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if (not l) and (not r): continue
            elif (not l) or (not r): return False
            elif l.val != r.val: return False
            else: stack += [(l.left, r.right), (l.right, r.left)]
        return True
