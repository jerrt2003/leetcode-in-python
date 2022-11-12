# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 64 ms, faster than 78.00% of Python online submissions for Delete N Nodes After M Nodes of a Linked List.
        Memory Usage: 17.2 MB, less than 61.00% of Python online submissions for Delete N Nodes After M Nodes of a Linked List.
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        _m = m
        while head:
            if _m == 0:
                k = n
                while k > 0 and head:
                    prev.next = head.next
                    head = head.next
                    k -= 1
                _m = m
            if not head:
                break
            prev = head
            head = head.next
            _m -= 1

        return dummy.next