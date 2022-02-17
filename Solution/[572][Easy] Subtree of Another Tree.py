# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if self.CheckSame(node, subRoot): return True
                stack += [node.left, node.right]
        return False

    def CheckSame(self, tree0, tree1):
        if (tree0 == None) and (tree1 == None): return True
        elif (tree0 != None) and (tree1 != None):
            return (tree0.val == tree1.val) and self.CheckSame(tree0.left, tree1.left) and self.CheckSame(tree0.right, tree1.right)
        else: return False
