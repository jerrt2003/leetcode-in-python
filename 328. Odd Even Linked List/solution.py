# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 24 ms, faster than 98.37% of Python online submissions for Odd Even Linked List.
        Memory Usage: 16.5 MB, less than 7.43% of Python online submissions for Odd Even Linked List.
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head