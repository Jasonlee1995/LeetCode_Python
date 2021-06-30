# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        if root == None: return True
        dic, stack = {None:0}, [root]
        while stack:
            node = stack[-1]
            if node in dic:
                if abs(dic[node.left] - dic[node.right]) > 1: return False
                dic[node] = max(dic[node.left], dic[node.right]) + 1
                stack.pop()
            else:
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                dic[node] = None
        return True
