# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root):
        stack = [root]
        vals = []
        while stack:
            node = stack.pop()
            if node:
                vals.append(node.val)
                stack += [node.left, node.right]
        vals.sort()

        answer = None
        for idx in range(len(vals)-1):
            if answer: answer = min(answer, vals[idx+1] - vals[idx])
            else: answer = vals[idx+1] - vals[idx]
            if answer == 0: break
        return answer
