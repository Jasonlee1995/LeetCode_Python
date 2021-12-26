# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        answer, stack = [], [root]
        while stack:
            temp_answer, temp_stack = [], []
            for node in stack:
                temp_answer.append(node.val)
                if node.left: temp_stack.append(node.left)
                if node.right: temp_stack.append(node.right)
            answer.append(sum(temp_answer)/len(temp_answer))
            stack = temp_stack
        return answer
