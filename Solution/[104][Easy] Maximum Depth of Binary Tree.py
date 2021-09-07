# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        stack = [(root, 1)]
        answer = 0
        while stack:
            node, num = stack.pop()
            if node == None: answer = max(answer, num-1)
            else: stack += [(node.left, num+1), (node.right, num+1)]
        return answer
