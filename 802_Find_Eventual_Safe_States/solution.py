class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        T:O(V+E) S:O(V)
        Runtime: 624 ms, faster than 75.09% of Python online submissions for Find Eventual Safe States.
        Memory Usage: 19.8 MB, less than 55.02% of Python online submissions for Find Eventual Safe States.
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        l = len(graph)
        visit = [0 for _ in range(l)]

        # def dfs(i):
        #     if visit[i] == -1:
        #         return False
        #     if visit[i] == 1:
        #         return True
        #     visit[i] = -1
        #     if all(dfs(nxt) for nxt in graph[i]):
        #         visit[i] = 1
        #         return True
        #     return False

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for nxt in graph[i]:
                if not dfs(nxt):
                    return False
            visit[i] = 1
            return True


        for i in range(l):
            if visit[i] == 0:
                dfs(i)

        ans = [k for k, v in enumerate(visit) if v != -1]
        return ans

print Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])