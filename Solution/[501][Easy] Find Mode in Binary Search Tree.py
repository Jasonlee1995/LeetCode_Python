# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root):
        stack = [root]
        infos = {}
        while stack:
            node = stack.pop()
            infos[node.val] = infos.get(node.val, 0) + 1
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        answer, count = [], max(infos.values())
        for val in infos:
            if infos[val] == count:
                answer.append(val)
        return answer
