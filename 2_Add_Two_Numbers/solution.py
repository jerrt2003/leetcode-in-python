from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        root = node
        carry = 0
        while l1 and l2:
            sum_val = l1.val + l2.val + carry
            carry, remainder = sum_val//10, sum_val%10
            new_node = ListNode(val=remainder)
            node.next = new_node
            node = node.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum_val = l1.val + carry
            carry, remainder = sum_val//10, sum_val%10
            new_node = ListNode(val=remainder)
            node.next = new_node
            node = node.next
            l1 = l1.next            
        while l2:
            sum_val = l2.val + carry
            carry, remainder = sum_val//10, sum_val%10
            new_node = ListNode(val=remainder)
            node.next = new_node
            node = node.next
            l2 = l2.next
        if carry:
            node.next = ListNode(val=carry)
        return root.next