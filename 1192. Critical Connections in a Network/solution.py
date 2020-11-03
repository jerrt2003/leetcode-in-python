import collections


class Solution(object):
    def criticalConnections(self, n, connections):
        """
        T:O(V+E) S:O(V+E)
        Runtime: 2092 ms, faster than 96.73% of Python online submissions for Critical Connections in a Network.
        Memory Usage: 87.8 MB, less than 50.99% of Python online submissions for Critical Connections in a Network.
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        # graph = collections.defaultdict(list)
        # for s, e in connections:
        #     graph[s].append(e)
        #     graph[e].append(s)
        #
        # edges = set(map(tuple, (map(sorted, connections))))
        # rank = [-2] * n
        #
        # def dfs(node, depth):
        #     if rank[node] >= 0:
        #         return rank[node]
        #     rank[node] = depth
        #     min_back_depth = n
        #     for nxt_node in graph[node]:
        #         if rank[nxt_node] == depth-1: # to avoid situation like 0->1->0, but 1 has other neighbor, so we need to continue
        #             continue
        #         back_depth = dfs(nxt_node, depth+1)
        #         if back_depth <= depth:
        #             edges.remove(tuple(sorted((node, nxt_node))))
        #         min_back_depth = min(min_back_depth, back_depth) # this line will let you know where does the loop started
        #     return min_back_depth
        #
        # dfs(0, 0)
        # return list(map(list, edges))

        graph = collections.defaultdict(list)
        node_depth = [0 for _ in range(n)]
        ans = []

        for s, e in connections:
            graph[s].append(e)
            graph[e].append(s)

        def dfs(node, parent, depth):
            node_depth[node] = depth
            for nxt_node in graph[node]:
                if nxt_node != parent:
                    if node_depth[nxt_node] == 0:
                        dfs(nxt_node, node, depth+1)
                    if node_depth[nxt_node] > depth:
                        ans.append([node, nxt_node])
                    else:
                        node_depth[node] = min(node_depth[node], node_depth[nxt_node])

        dfs(0, -1, 1)
        return ans

print Solution().criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])