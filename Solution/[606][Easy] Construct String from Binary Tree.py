# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root):
        if not root: return ''
        answer = str(root.val)
        if root.left or root.right:
            answer += '({})'.format(self.tree2str(root.left))
        if root.right:
            answer += '({})'.format(self.tree2str(root.right))
        return answer
