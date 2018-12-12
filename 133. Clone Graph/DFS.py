# -*- coding: utf-8 -*-
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).
        TP:
        - very similar to LT_138
        - Create a dict to store visited node
        - During the DFS
            - if a node is visited, simply add that node into "THIS" recursion node's neighbor
            - elif a node is not visited, then:
                - create a new_node with new_node.label = neighbor_node.label
                - add this this node into self.visited: self.visited[neighbor] = new_node
                - append new_node into copy's node neighbor_list
        :param node:
        :return:
        """
        if node is None: return None
        self.visited = dict()
        copy_head = UndirectedGraphNode(node.label)
        self.visited[node] = copy_head
        self.dfs(node)
        return copy_head

    def dfs(self, node):
        for neighbor in node.neighbors:
            if neighbor in self.visited:
                self.visited[node].neighbors.append(self.visited[neighbor])
            else:
                copy_neighbor = UndirectedGraphNode(neighbor.label)
                self.visited[neighbor] = copy_neighbor
                self.visited[node].neighbors.append(copy_neighbor)
                self.dfs(neighbor)




