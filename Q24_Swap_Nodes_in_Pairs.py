# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        HINT: recursion
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        tmp = ListNode(head.next.val)
        head.next = self.swapPairs(head.next.next)
        tmp.next = head
        return tmp
