"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Dict, Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Optional[Node]:
        if not node:
            return None
        # use an hashmap to store org_node and clone_node
        # use a queue for BFS
        clone_map: Dict[Node, Node] = {}
        clone = Node(node.val, [])
        clone_map[node] = clone
        q = [node]
        # BFS
        while q:
            tmp_node = q.pop(0)
            for neighbor in tmp_node.neighbors:
                if neighbor not in clone_map.keys():
                    clone_node = Node(neighbor.val, [])
                    clone_map[neighbor] = clone_node
                    clone_map[tmp_node].neighbors.append(clone_node)
                    q.append(neighbor)
                else:
                    clone_map[tmp_node].neighbors.append(clone_map[neighbor])
        return clone