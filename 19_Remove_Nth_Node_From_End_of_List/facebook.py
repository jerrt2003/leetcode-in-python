# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = p2 = head
        while n > 0:
            p2 = p2.next
            n -= 1
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while p2:
            prev = p1
            p1 = p1.next
            p2 = p2.next
        prev.next = p1.next
        return dummy.next