# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        Perf: Runtime: 12 ms, faster than 99.50% / Memory Usage: 11.8 MB, less than 67.82%
        T: O(n)
        S: O(n)
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode(None)
        head = node
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        while l1:
            node.next = l1
            l1 = l1.next
            node = node.next

        while l2:
            node.next = l2
            l2 = l2.next
            node = node.next

        return head.next