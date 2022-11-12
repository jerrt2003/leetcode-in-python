# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        Solution: BFS
        Time Complexity: O(n) (n: number of tree nodes)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        TP:
        - Traverse the tree using BFS
            - while traversing, we will use:
                - direction to denote which direction we are:
                    - 1 means left to right
                    - -1 means right to left
                - a list called "next_queue" which will store next level nodes
                - depends on traverse direction of this level, we will decide if left node should come first or right node will come first
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        queue = [root]
        res = []
        direction = 1
        def BFS(queue, res, direction):
            next_queue = []
            path = []
            if direction > 0:
                for q in queue[::-1]: # !!!!!! remember to reverse the queue
                    if q.left: next_queue.append(q.left)
                    if q.right: next_queue.append(q.right)
                    path.append(q.val)
            else:
                for q in queue[::-1]: # !!!!!! remember to reverse the queue
                    if q.right: next_queue.append(q.right)
                    if q.left: next_queue.append(q.left)
                    path.append(q.val)
            direction = direction * -1
            res.append(path)
            return next_queue, res, direction

        while queue:
            queue, res, direction = BFS(queue, res, direction)

        return res

def stringToTreeNode(inputValues):
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


#nodes = [3,9,20,'null','null',15,7]
nodes = [0,2,4,1,'null',3,-1,5,1,'null',6,'null',8]
print Solution().zigzagLevelOrder(stringToTreeNode(nodes))
