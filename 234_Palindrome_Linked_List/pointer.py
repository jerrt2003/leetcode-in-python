from typing import Optional

from common.list_node import ListNode

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 當fast不為None,說明鍊錶長度為奇數
        if fast:
            slow = slow.next
        
        slow = self.reverse(slow)
        fast = head
        while slow:
            if fast.val != slow.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
    
    def reverse(self, head: ListNode) -> ListNode:
        """反轉LinkedList

        Args:
            head (ListNode):

        Returns:
            ListNode:
        """
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev