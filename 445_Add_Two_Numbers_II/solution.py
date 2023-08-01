# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1 = self.reverse_linked_list(l1)
        l2 = self.reverse_linked_list(l2)
        dummy = ListNode()
        prev = dummy

        carry_over = 0
        while l1 and l2:
            total = l1.val + l2.val + carry_over
            carry_over = total // 10
            remainder = total % 10
            node = ListNode(val=remainder)
            prev.next = node
            prev = prev.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + carry_over
            carry_over = total // 10
            remainder = total % 10
            node = ListNode(val=remainder)
            prev.next = node
            prev = prev.next
            l1 = l1.next

        while l2:
            total = l2.val + carry_over
            carry_over = total // 10
            remainder = total % 10
            node = ListNode(val=remainder)
            prev.next = node
            prev = prev.next

            l2 = l2.next

        if carry_over != 0:
            node = ListNode(val=carry_over)
            prev.next = node
            prev = prev.next

        return self.reverse_linked_list(dummy.next)

    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev
