# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        Solution: 2 pointer (龜兔賽跑)
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By:
        - https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
        TP:
        - 2 pointer: slow and fast
        - for each iteration:
            - slow will move 1 step forward
            - fast will move 2 step forward
            - slow and fast will meet eventually if there is a loop
        :type head: ListNode
        :rtype: bool
        """
        a = head
        b = head
        while a is not None and b is not None and b.next is not None:
            a = a.next
            b = b.next.next
            if a == b:
                return True
        return False