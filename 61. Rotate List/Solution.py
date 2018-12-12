# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        Solution: 2 pass + rotate
        Time Complexity: O(2n) -> O(n)
        Space Complexity: O(1)
        Inspired by: https://leetcode.com/problems/rotate-list/discuss/22715/Share-my-java-solution-with-explanation
        TP:
        - Solution contain 3 steps:
            - 1. Find the total length of linked list
            - 2. Based on length to decide i-th element will be the new end node of linked list
            - 3. Rotate the linked list
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k == 0: return head
        dummy = ListNode(0)
        dummy.next = head
        fast = head
        slow = head

        i = 1
        while fast.next is not None:
            fast = fast.next
            i += 1

        rotate_node = i - k%i -1

        for _ in range(rotate_node):
            slow = slow.next

        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None

        return dummy.next

first = ListNode(0)
second = ListNode(1)
third = ListNode(2)
first.next = second
second.next = third

print Solution().rotateRight(first, 4)
