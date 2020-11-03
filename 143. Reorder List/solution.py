# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 96 ms, faster than 76.71% of Python online submissions for Reorder List.
        Memory Usage: 32.9 MB, less than 34.26% of Python online submissions for Reorder List.
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # find the 2nd half of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half of the list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        a = head
        b = prev
        while b.next:
            tmp = a.next
            a.next = b
            a = tmp
            tmp = b.next
            b.next = a
            b = tmp

        return head
