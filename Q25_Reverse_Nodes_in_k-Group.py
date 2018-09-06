#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        current = head
        for i in range(k):
            if current is None:
                return head
            else:
                current = current.next
        current = self.reverseKGroup(current, k)
        for i in range(k):
            tmp = head.next
            head.next = current
            current = head
            head = tmp
        return current

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

sol = Solution()

tmp = sol.reverseKGroup(a, 2)
print tmp.val, tmp.next

