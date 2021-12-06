"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
        if not root: return []
        stack = [root]
        answer = []
        while stack:
            node = stack.pop()
            answer.append(node.val)
            if node.children: stack += node.children[::-1]
        return answer
