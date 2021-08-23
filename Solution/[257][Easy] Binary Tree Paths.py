# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        stack = [([str(root.val)], root)]
        answer = []
        while stack:
            val_list, node = stack.pop()
            if (node.left == None) and (node.right == None): answer.append('->'.join(val_list))
            else:
                if node.left != None: stack.append((val_list + [str(node.left.val)], node.left))
                if node.right != None: stack.append((val_list + [str(node.right.val)], node.right))
        return answer
