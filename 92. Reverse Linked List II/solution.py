# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 12 ms, faster than 98.37% of Python online submissions for Reverse Linked List II.
        Memory Usage: 13 MB, less than 17.83% of Python online submissions for Reverse Linked List II.
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, dummy.next
        beforeM, afterN = None, None
        nodeM, nodeN = None, None
        cnt = 1
        while cnt <= n:
            nxt = curr.next
            if cnt == m:
                beforeM = prev
                nodeM = curr
            if cnt == n:
                afterN = nxt
                nodeN = curr
            if m < cnt <= n:
                curr.next = prev
            prev, curr = curr, nxt
            cnt += 1

        beforeM.next = nodeN
        nodeM.next = afterN

        return dummy.next