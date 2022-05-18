# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.curr.right = node
                self.curr = self.curr.right
                inorder(node.right)
        
        answer = self.curr = TreeNode(None)
        inorder(root)
        return answer.right
