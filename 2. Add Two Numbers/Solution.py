# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Solution: Linked List
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        TP:
        - Adding each digit and take extra care for the carry over !!
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp_head = ListNode(0)
        head = tmp_head
        carry_over = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry_over
            carry_over = sum / 10
            digit = sum % 10
            new_node = ListNode(digit)
            head.next = new_node
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            sum = l1.val + carry_over
            carry_over = sum / 10
            digit = sum % 10
            new_node = ListNode(digit)
            head.next = new_node
            head = head.next
            l1 = l1.next
        while l2 is not None:
            sum = l2.val + carry_over
            carry_over = sum / 10
            digit = sum % 10
            new_node = ListNode(digit)
            head.next = new_node
            head = head.next
            l2 = l2.next
        if carry_over != 0:
            new_node = ListNode(carry_over)
            head.next = new_node
        return tmp_head.next

