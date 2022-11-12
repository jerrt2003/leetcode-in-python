class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insert(self, head, insertVal):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 24 ms, faster than 72.31% of Python online submissions for Insert into a Sorted Circular Linked List.
        Memory Usage: 13.3 MB, less than 100.00% of Python online submissions for Insert into a Sorted Circular Linked List.
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        new_node = Node(insertVal)
        if head is None:
            new_node.next = new_node
            return new_node

        dummy = head
        while True:
            if head.val <= insertVal <= head.next.val:
                break
            elif head.next == dummy:
                break
            elif head.val > head.next.val and (insertVal >= head.val or insertVal <= head.next.val):
                break
            head = head.next

        new_node.next = head.next
        head.next = new_node
        return dummy


