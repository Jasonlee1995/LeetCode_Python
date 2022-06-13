# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low, high):
        if not root: return 0
        l, r = self.rangeSumBST(root.left, low, high), self.rangeSumBST(root.right, low, high)
        if root.val > high: return l
        elif root.val < low:  return r
        else: return root.val + l + r
        