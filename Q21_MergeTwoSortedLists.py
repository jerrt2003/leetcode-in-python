# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head = None
        current = None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while l1 != None and l2 != None:
            if head == None:
                if l1.val <= l2.val:
                    head = l1
                    current = l1
                    l1 = l1.next
                else:
                    head = l2
                    current = l2
                    l2 = l2.next
            else:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
        while l1 != None:
            current.next = l1
            l1 = l1.next
            current = current.next
        while l2 != None:
            current.next = l2
            l2 = l2.next
            current = current.next
        return head

a1 = ListNode(1)
b1 = ListNode(2)
b2 = ListNode(3)
b1.next = b2

sol = Solution()
head = sol.mergeTwoLists(a1, b1)
while head != None:
    print(head.val)
    head = head.next