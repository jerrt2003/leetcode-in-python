# -*- coding: utf-8 -*-
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!!
        TP:
        - Using stack-like data structure to pass along in the recursion
        :param root:
        :return:
        """
        if root is None: return None
        self.assignToNext([root])
        print(root)

    def assignToNext(self, nodes):
        if nodes is None or len(nodes) == 0:
            return
        next_level_nodes = []
        for i in range(len(nodes)):
            if nodes[i].left is not None:
                next_level_nodes.append(nodes[i].left)
            if nodes[i].right is not None:
                next_level_nodes.append(nodes[i].right)
            if i < len(nodes)-1:
                nodes[i].next = nodes[i+1]
            else:
                nodes[i].next = None
        self.assignToNext(next_level_nodes)


node_1 = TreeLinkNode(1)
node_2 = TreeLinkNode(2)
node_3 = TreeLinkNode(3)
node_4 = TreeLinkNode(4)
node_5 = TreeLinkNode(5)
node_7 = TreeLinkNode(7)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_2.right = node_5
node_3.right = node_7

sol = Solution()
sol.connect(node_1)
