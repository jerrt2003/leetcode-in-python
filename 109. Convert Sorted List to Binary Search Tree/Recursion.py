# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        Solution: recursion
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!!
        TP:
        - a BST definition: a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1
        - First we need to convert linked-list to a list of value
        - Then we can start conver this list to BST by:
            - If the input list len is 0 which means we have no node, thus return None
            - If the input list len is 1 which means we have only one node, then we return this node (TreeNode)
            - Otherwise go through following steps:
                - Find out the mid-point, this will be our root node for current tree
                - convert list[0:mid-point] and its return will be the left node
                - convert list[mid-point+1:end_of_list] and its return will be the right node
                - return root node
        :type head: ListNode
        :rtype: TreeNode
        """
        nodes = []
        if head is None:
            return None
        while head is not None: # convert linked-list to val list
            nodes.append(head.val)
            head = head.next
        return self.convert(nodes)

    def convert(self, nodes):
        """
        To convert a list to BST
        :param nodes:
        :return:
        """
        nodes_len = len(nodes)
        if nodes_len == 0: return None
        if nodes_len == 1: return TreeNode(nodes[0])
        mid = nodes_len/2
        node = TreeNode(nodes[mid])
        node.left = self.convert(nodes[0:mid])
        node.right = self.convert(nodes[mid+1:nodes_len])
        return node
