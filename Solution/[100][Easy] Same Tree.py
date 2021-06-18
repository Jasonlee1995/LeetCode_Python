# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            node0, node1 = stack.pop()
            if (not node0) and (not node1): continue
            elif (not node0) or (not node1): return False
            elif node0.val != node1.val: return False
            else: stack += [(node0.left, node1.left), (node0.right, node1.right)]
        return True
