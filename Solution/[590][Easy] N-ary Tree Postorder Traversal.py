"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root):
        if not root: return []
        stack = [root]
        answer = []
        while stack:
            node = stack.pop()
            stack += node.children
            answer.append(node.val)
        return answer[::-1]
