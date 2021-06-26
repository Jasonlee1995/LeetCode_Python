# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0: return None
        start, end = 0, len(nums)-1
        center = (start + end) // 2
        answer = TreeNode(nums[center])

        stack = []
        if start != center: stack.append((start, center-1, answer, 'left'))
        if center != end: stack.append((center+1, end, answer, 'right'))

        while stack:
            start, end, node, l_r = stack.pop()
            mid = (start + end) // 2
            if l_r == 'left':
                node.left = TreeNode(nums[mid])
                node = node.left
            elif l_r == 'right':
                node.right = TreeNode(nums[mid])
                node = node.right

            if start != mid: stack.append((start, mid-1, node, 'left'))
            if mid != end: stack.append((mid+1, end, node, 'right'))
        return answer
