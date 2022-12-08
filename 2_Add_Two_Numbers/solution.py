from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        node = root
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            curr_sum = l1_val + l2_val + carry
            carry, remainder = curr_sum//10, curr_sum%10
            node.next = ListNode(val=remainder)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            node = node.next
        if carry:
            node.next = ListNode(val=carry)
        return root.next