# -*- coding: utf-8 -*-
class Solution(object):
    def detectCycle(self, head):
        """
        T:O(n)
        S:O(1)
        Perf: Runtime: 28 ms, faster than 99.55% / Memory Usage: 18.1 MB, less than 84.91%
        :type head: ListNode
        :rtype: ListNode
        """
        pt1, pt2 = head, head
        while pt1 and pt2 and pt1.next and pt2.next and pt2.next.next:
            pt1 = pt1.next
            pt2 = pt2.next.next
            if pt1 == pt2:
                A = head
                B = pt2
                while A != B:
                    A = A.next
                    B = B.next
                return A
        return None
