# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        Solution: 1 pass with dummy nodes
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/partition-list/discuss/29174/Python-concise-solution-with-dummy-nodes
        TP:
        - create 4 nodes h1, l1, h2, l2
            - h1, h2 are used to preserve starting nodes
            - l1, l2 are used to move along when we move head
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head is not None:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next