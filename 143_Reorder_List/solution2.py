# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        l, r = 0, len(nodes) - 1

        while l < r:
            nodes[l].next = nodes[r]
            nodes[r].next = nodes[l + 1]
            l += 1
            r -= 1

        nodes[l].next = None

        return nodes[0]
