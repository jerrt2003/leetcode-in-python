import collections
from typing import Dict, List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited: List[int] = [0 for _ in range(n)]
        adjacency_list: Dict[int, List[int]] = collections.defaultdict(list)
        for edge in edges:
            s, e = edge[0], edge[1]
            adjacency_list[s].append(e)
            adjacency_list[e].append(s)
        ans = 0
        for i in range(n):
            if visited[i] == 0:
                ans += 1
                visited[i] = 1
                q = [i]
                while q:
                    cur_node = q.pop(0)
                    for neighbor in adjacency_list[cur_node]:
                        if visited[neighbor] == 0:
                            visited[neighbor] = 1
                            q.append(neighbor)

        return ans
