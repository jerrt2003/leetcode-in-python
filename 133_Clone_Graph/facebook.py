"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        Facebook
        DFS
        T:O(n) S:O(n)
        Runtime: 52 ms, faster than 27.13% of Python online submissions for Clone Graph.
        Memory Usage: 13.1 MB, less than 43.97% of Python online submissions for Clone Graph.
        :type node: Node
        :rtype: Node
        """
        # nodeMap = dict()
        #
        # def dfs(node):
        #     newNode = Node(node.val)
        #     nodeMap[node] = newNode
        #     for nei in node.neighbors:
        #         if nei in nodeMap:
        #             newNode.neighbors.append(nodeMap[nei])
        #         else:
        #             newNode.neighbors.append(dfs(nei))
        #     return newNode
        #
        # if not node:
        #     return None
        # return dfs(node)
        old2new = {}
        newNode = Node(node.val)
        old2new[node] = newNode
        q = collections.deque([node])
        while q:
            curr = q.popleft()
            for nei in node.neighbors:
                if nei in old2new:
                    old2new[curr].neighbors.append(old2new[nei])
                else:
                    new_nei = Node(nei.val)
                    old2new[curr].neighbors.append(new_nei)
                    q.append(nei)

        return newNode