# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root, x, y):
        stack = [(None, root)]
        while stack:
            vals, childs = {}, []
            for parent_val, node in stack:
                vals[node.val] = parent_val
                if node.left: childs.append((node.val, node.left))
                if node.right: childs.append((node.val, node.right))
            
            x_in, y_in = vals.get(x), vals.get(y)
            if x_in and y_in:
                if x_in == y_in: return False
                else: return True
            elif (not x_in) and (not y_in):
                stack = childs
            else:
                return False
        return False