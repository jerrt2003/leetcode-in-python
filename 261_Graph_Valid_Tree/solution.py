import collections

from typing import List, Dict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n nodes require n-1 edges to form valid tree
        if n-1 != len(edges):
            return False

        # tree def: all nodes are connected + all node pairs has only one edge
        # create hashmap: neighbors to record nodes' neighbors
        # create set: visited to record 'visited' nodes
        # create q for BFS, place any point (e.g. 0) to the queue and place it into 'visited' SET
        neighbors: Dict[int, List[int]] = collections.defaultdict(list)
        for e1, e2 in edges:
            neighbors[e1].append(e2)
            neighbors[e2].append(e1)
        q = [0]
        visited = set([0])

        # BFS
        while q:
            node = q.pop(0)
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        return len(visited) == n