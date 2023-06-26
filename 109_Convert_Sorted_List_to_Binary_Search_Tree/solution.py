# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.node_val: List[int] = []
        while head:
            self.node_val.append(head.val)
            head = head.next

        s, e = 0, len(self.node_val) - 1
        return self.helper(s, e)

    def helper(self, s: int, e: int) -> Optional[TreeNode]:
        if s > e:
            return None
        mid = (s + e) // 2
        node = TreeNode(val=self.node_val[mid])
        node.left = self.helper(s, mid - 1)
        node.right = self.helper(mid + 1, e)
        return node
