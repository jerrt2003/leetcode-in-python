__author__ = 'dcheng'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        previous = head
        start = head
        end = head
        for i in range(n-1):
            if end.next != None:
                end = end.next
            else:
                return head
        if end.next == None: # handle the case where the element to be deleted is the 1st element
            head = head.next
            return head
        while end.next != None:
            previous = start
            start = start.next
            end = end.next
        previous.next = start.next
        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

remove = Solution()
head = remove.removeNthFromEnd(a,3)
