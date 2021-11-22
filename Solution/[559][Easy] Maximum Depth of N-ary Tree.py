"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root):
        if not root: return 0
        stack = [(root, 1)]
        while stack:
            temp_stack = []
            for node, depth in stack:
                if node.children == None: continue
                for child_node in node.children:
                    temp_stack.append((child_node, depth+1))

            if temp_stack: stack = temp_stack
            else: return depth
