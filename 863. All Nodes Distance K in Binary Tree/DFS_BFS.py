# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        Solution: DFS + BFS
        Time Complexity: O(n) --> https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/143729/Python-DFS-and-BFS/150728
        Space Complexity: O(2n + n)
        Inspired By: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/143729/Python-DFS-and-BFS
        TP:
        - To build a 'connection' mapping of all nodes
        - Then we can use do K times of BFS to get all nodes
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if not root: return []
        import collections
        conn = collections.defaultdict(list)
        def DFS(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: DFS(child, child.left)
            if child.right: DFS(child, child.right)
        DFS(None, root)
        q = [target]
        visited = set(q)
        for i in range(K):
            for j in range(len(q)):
                curr = q.pop(0)
                visited.add(curr)
                for node in conn[curr]:
                    if node not in visited:
                        q.append(node)
        return q


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

root = stringToTreeNode([3,5,1,6,2,0,8,'null','null',7,4])
#root = []
target = 5
K = 2

print Solution().distanceK(root, target, K)