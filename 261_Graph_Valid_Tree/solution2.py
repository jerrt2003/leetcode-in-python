import collections
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        node_2_node_map = collections.defaultdict(list)
        for edge in edges:
            s, e = edge[0], edge[1]
            node_2_node_map[s].append(e)
            node_2_node_map[e].append(s)
        q = [0]
        visited = set(q)
        while q:
            node = q.pop(0)
            # 在无向图中，对于任意一条边，比如边(a, b)，在访问顺序中，无论是先访问节点a再访问节点b，还是先访问节点b再访问节点a，节点a和节点b都是彼此的邻居。因此，当你从节点a访问到节点b，然后试图回到节点a时，会发现节点a已经在访问过的节点集合中了，此时返回 False 就判定错误了。
            # 换句话说，如果你正在处理节点a，并且在处理其邻居时发现一个已经访问过的邻居b，那并不意味着这是一个环，因为在无向图中，b的邻居中应当就包含a。
            # 因此，在这个函数中，我们并不能只是简单地检查邻居是否已经被访问过，而需要做更复杂的环检测。
            for neighbor in node_2_node_map[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return len(visited) == n
