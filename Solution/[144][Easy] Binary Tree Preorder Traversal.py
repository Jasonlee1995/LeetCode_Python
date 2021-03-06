# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        if root == None: return []
        stack, answer = [root], []
        while stack:
            node = stack.pop()
            answer.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return answer
