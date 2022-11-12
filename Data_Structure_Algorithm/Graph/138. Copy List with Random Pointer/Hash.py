# -*- coding: utf-8 -*-
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def __init__(self):
        self.visted = {}

    def copyRandomList(self, head):
        """
        Solution: Hash
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/copy-list-with-random-pointer/solution/
        TP:
        - 問題點在於怎麼處理所謂的random node, 因為random node有可能會指向自己, 造成無限迴圈
        - 處理方式：利用dict去紀錄已經visit過的node, 假如已經在了, 我們就用那個node作為ref
        - dict's key: old_node, value: new_node
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        old_node = head
        new_node = RandomListNode(old_node.label)
        self.visted[old_node] = new_node
        while old_node:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)
            old_node = old_node.next
            new_node = new_node.next
        return self.visted[head]

    def getClonedNode(self, node):
        if node:
            if self.visted.has_key(node):
                return self.visted[node]
            else:
                self.visted[node] = RandomListNode(node.label)
                return self.visted[node]
        return None