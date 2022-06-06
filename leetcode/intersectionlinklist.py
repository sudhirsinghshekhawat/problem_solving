# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length_a = self.length_linklist(headA)
        length_b = self.length_linklist(headB)

        if length_a > length_b:
            longer = headA
            shorter = headB
        else:
            longer = headB
            shorter = headA

        diff = abs(length_a - length_b)

        for i in range(diff):
            longer = longer.next

        result = None
        while longer and shorter:
            if longer == shorter:
                result = longer.val
                break
            longer = longer.next
            shorter = shorter.next

        return result

    def length_linklist(self, node):
        temp = node
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length

    def getIntersectionNode_1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
