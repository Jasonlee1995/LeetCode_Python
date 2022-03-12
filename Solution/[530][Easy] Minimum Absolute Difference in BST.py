# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root):
        def inorder(node):
            order = []
            if node.left: order += inorder(node.left)
            order.append(node.val)
            if node.right: order += inorder(node.right)
            return order

        vals = inorder(root)
        answer = min(vals[i+1] - vals[i] for i in range(len(vals)-1))
        return answer
