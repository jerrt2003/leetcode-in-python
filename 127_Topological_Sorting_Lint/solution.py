import collections
from typing import Dict, List

class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph: List[DirectedGraphNode]) -> List[DirectedGraphNode]:
        ret = []
        in_degree: Dict[DirectedGraphNode, int] = collections.defaultdict(int)
        # build indgree maps
        for node in graph:
            in_degree[node] = 0
            for neighbor in node.neighbors:
                in_degree[neighbor] += 1
        # check which nodes' indgree == 0 (pick root nodes) and place into init queue
        q = []
        for k, v in in_degree.items():
            if v == 0:
                q.append(k)
        # start BFS, once node is visited, place into the sorted order
        # and all its neighbors' indegree reduced by 1
        # only when a node's indgree == 0 push into the queue
        while q:
            node = q.pop(0)
            ret.append(node)
            for neighbor in node.neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        return ret
