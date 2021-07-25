# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        def get_len(Node):
            len_Node = 0
            while Node:
                len_Node += 1
                Node = Node.next
            return len_Node

        currA, currB = headA, headB
        lenA, lenB = get_len(currA), get_len(currB)

        for _ in range(abs(lenA - lenB)):
            if lenA > lenB: headA = headA.next
            else: headB = headB.next

        while True:
            if headA == headB: return headA
            else: headA, headB = headA.next, headB.next
