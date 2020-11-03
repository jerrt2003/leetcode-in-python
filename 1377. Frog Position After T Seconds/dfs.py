import collections

class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        DFS
        T:O(nlogn)+O(n) S:O(n)
        Runtime: 76 ms, faster than 68.93% of Python online submissions for Frog Position After T Seconds.
        Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Frog Position After T Seconds.
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        graph = collections.defaultdict(list)
        for edge in edges:
            edge = sorted(edge)
            graph[edge[0]].append(edge[1])

        def dfs(id, cost, t):
            if id == target and (t == 0 or id not in graph):
                return cost
            elif t == 0:
                return 0
            else:
                for nxt_id in graph[id]:
                    ret = dfs(nxt_id, cost*(1.0/len(graph[id])), t-1)
                    if ret != 0:
                        return ret
                return 0

        return dfs(1, 1, t)

print Solution().frogPosition(7,[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]],2,4)
print Solution().frogPosition(3,[[2,1],[3,2]],1,2)
print Solution().frogPosition(3,[[2,1],[3,2]],1,2)
print Solution().frogPosition(8,[[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]],7,7)
print Solution().frogPosition(7,[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]],20,6)