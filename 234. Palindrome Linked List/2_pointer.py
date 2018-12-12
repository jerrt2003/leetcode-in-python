# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        Solution: Use 2 pointer to achieve O(n) time and O(1) space
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/palindrome-linked-list/discuss/64501/Java-easy-to-understand
        TP:
        - First use 2 pointer: slow, fast to find the mid point
            - slow will move one node at a time
            - fast will move 2 nodes at a time
        - Once find the mid node, reverse the 2nd half
            - !!! need to consider odd nodes situation
            - if we have odd nodes (e.g. [1,2,1]) then we just need to move mid node one node ahead
        - Once node reverse, go through the linked list to compare node val one by one
        :type head: ListNode
        :rtype: bool
        """
        def reverse(head):
            prev = None
            while head is not None:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast is not None:
            slow = slow.next
        ptr1 = head
        ptr2 = reverse(slow)
        while ptr2 is not None: # !!! WHY ptr2 --> because only ptr2 will hit None situation (since we reverse the node already)
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return True

