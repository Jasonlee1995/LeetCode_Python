# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root):
        def recursion(node, val):
            val = 2 * val + node.val
            if (node.left == None) and (node.right == None):
                return val
            elif (node.left == None) and (node.right != None):
                return recursion(node.right, val)
            elif (node.left != None) and (node.right == None):
                return recursion(node.left, val)
            else:
                return recursion(node.left, val) + recursion(node.right, val)
        return recursion(root, 0)