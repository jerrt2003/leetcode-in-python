# Definition for singly-linked list.
import collections
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 這段代碼的主要目的是將給定的單鏈表向右旋轉k個位置。換句話說，我們將鏈表的尾部向前移動k個位置來成為新的頭部。
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        _len = 0
        cur = head
        while cur:
            _len += 1
            cur = cur.next

        k = k % _len

        if k == 0:
            return head

        slow, fast = head, head
        while k > 0:
            fast = fast.next
            k -= 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None

        fast.next = head

        return new_head
