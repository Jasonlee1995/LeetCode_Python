# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        stack, answer = [(root, True)], []
        while stack:
            node, check = stack.pop()
            if node != None:
                if check: stack += [(node.right, True), (node, False), (node.left, True)]
                else: answer.append(node.val)
        return answer
