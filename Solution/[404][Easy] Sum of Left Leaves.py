# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        stack = [(root, False)]
        answer = 0
        while stack:
            node, tf = stack.pop()
            if node.left: stack.append((node.left, True))
            if node.right: stack.append((node.right, False))
            if (node.left == None) and (node.right == None) and tf: answer += node.val
        return answer
