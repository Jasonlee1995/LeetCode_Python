# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        candidates = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val == subRoot.val: candidates.append(node)
                stack += [node.left, node.right]

        for candidate in candidates:
            temp_c, temp_s = [candidate], [subRoot]
            while temp_c and temp_s:
                node_c, node_s = temp_c.pop(), temp_s.pop()
                if (node_c == None) and (node_s == None): continue
                elif (node_c != None) and (node_s != None):
                    if node_c.val == node_s.val:
                        temp_c += [node_c.left, node_c.right]
                        temp_s += [node_s.left, node_s.right]
                    else: break
                else: break
            else:
                if temp_c == temp_s:
                    return True
        return False
