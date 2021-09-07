# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def minDepth(self, root):
        if root == None: return 0
        deque = collections.deque([(root, 1)])
        while deque:
            node, depth = deque.popleft()
            if (node.left == None) and (node.right == None): return depth
            if node.left: deque.append((node.left, depth+1))
            if node.right: deque.append((node.right, depth+1))
