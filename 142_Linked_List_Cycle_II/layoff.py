from typing import Optional
from common.list_node import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                tmp_pt = head
                while tmp_pt != slow:
                    tmp_pt = tmp_pt.next
                    slow = slow.next
                return slow
        return None