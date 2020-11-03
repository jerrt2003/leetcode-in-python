# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        facebook
        T:O(n) S:O(1)
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head:
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            head2 = None
            while slow:
                nxt = slow.next
                slow.next = head2
                head2 = slow
                slow = nxt

            while head2.next:
                head.next, head = head2, head.next
                head2.next, head2 = head, head2.next