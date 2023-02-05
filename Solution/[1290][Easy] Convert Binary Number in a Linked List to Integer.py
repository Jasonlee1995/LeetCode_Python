# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head):
        num = 0
        while head:
            num = 2 * num + head.val
            head = head.next
        return num
