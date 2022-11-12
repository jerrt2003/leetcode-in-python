# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, G):
        """
        T:O(n) S:O(n)
        Runtime: 112 ms, faster than 37.85% of Python online submissions for Linked List Components.
        Memory Usage: 20.6 MB, less than 11.11% of Python online submissions for Linked List Components.
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        count = 0
        on_streak = False
        while head is not None:
            if head.val in G and not on_streak:
                on_streak = True
            elif head.val not in G and on_streak:
                on_streak = False
                count += 1
            head = head.next
        if on_streak:
            count += 1
        return count