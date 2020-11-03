# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        T:O(nlogn) S:O(logn)
        Runtime: 232 ms, faster than 80.79% of Python online submissions for Sort List.
        Memory Usage: 29.7 MB, less than 77.45% of Python online submissions for Sort List.
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        l = self.sortList(head)
        r = self.sortList(slow)
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = ListNode()
        p = dummy

        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next

        while l:
            p.next = l
            l = l.next
            p = p.next

        while r:
            p.next = r
            r = r.next
            p = p.next

        return dummy.next
