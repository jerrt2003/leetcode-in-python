# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Sol: using stack (FILO)
        Time: O(n)
        Space: O(n)
        Perf: Runtime: 64 ms, faster than 92.01% / Memory Usage: 11.7 MB, less than 96.02%
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        last = None
        total = 0
        while stack1 or stack2:
            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()
            node = ListNode(total % 10)
            node.next = last
            last = node
            total = total / 10
        if total != 0:
            node = ListNode(total)
            node.next = last
            last = node
        return last

