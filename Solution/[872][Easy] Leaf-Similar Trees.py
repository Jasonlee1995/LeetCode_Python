# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(root):
            stack, leaf = [root], []
            while stack:
                node = stack.pop()
                if (node.left == None) and (node.right == None): leaf.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            return leaf
        return dfs(root1) == dfs(root2)
