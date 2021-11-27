# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root):
        tilt, _ = self.recursion(root)
        return tilt

    def recursion(self, node):
        if node == None: return 0, 0
        left_tilt, left_sum = self.recursion(node.left)
        right_tilt, right_sum = self.recursion(node.right)
        node_tilt = left_tilt + right_tilt + abs(left_sum - right_sum)
        node_sum = left_sum + right_sum + node.val
        return node_tilt, node_sum
