# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        Solution: O(n) --> TLE
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        TP:
        - create a list, record visited
        :type head: ListNode
        :rtype: bool
        """
        visited = []
        while head is not None:
            if head in visited:
                return True
            visited.append(head)
            head = head.next
        return False
