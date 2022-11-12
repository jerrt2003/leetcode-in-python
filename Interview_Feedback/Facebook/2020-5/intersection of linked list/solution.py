class Solution(object):
    def findIntersectionOfLinkedList(self, n1, n2):
        c1 = 0
        while n1:
            c1 += 1
            n1 = n1.next
        c2 = 0
        while n2:
            c2 += 1
            n2 = n2.next

        diff = abs(c1-c2)
        node1 = n1 if c1 > c2 else n2
        node2 = n1 if node1 == n1 else n2

        while n1 > 0:
            n1 -= 1
            node1 = node1.next

        while node1 and node2:
            if node1 == node2:
                return node1.val
            node1 = node1.next
            node2 = node2.next