# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(-1, head)
        current = dummy
        while current:
            if current.next and (current.next.val == val): current.next = current.next.next
            else: current = current.next
        return dummy.next
