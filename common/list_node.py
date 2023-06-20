class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val

def reverse(self, node: ListNode) -> ListNode:
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


