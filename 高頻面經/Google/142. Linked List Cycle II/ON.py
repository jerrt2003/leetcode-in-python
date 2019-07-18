# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        Solution: O(n)
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By:
        - https://leetcode.com/problems/linked-list-cycle-ii/solution/ (!! very helpful, go read it)
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        slow = fast = ptr1 = head
        while slow.next is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ptr2 = slow
                while ptr1 != ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next
                return ptr1
        return None

