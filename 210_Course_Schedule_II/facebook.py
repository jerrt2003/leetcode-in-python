import collections


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 84 ms, faster than 86.81% of Python online submissions for Course Schedule II.
        Memory Usage: 16.4 MB, less than 12.28% of Python online submissions for Course Schedule II.
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visit = [0] * numCourses

        graph = collections.defaultdict(list)
        for e, s in prerequisites:
            graph[s].append(e)

        def dfs(c, path):
            if visit[c] == -1:
                return False
            if visit[c] == 1:
                return True
            visit[c] = -1
            for nei in graph[c]:
                if not dfs(nei, path):
                    return False
            visit[c] = 1
            path.append(c)
            return True

        path = []
        for i in range(numCourses):
            if visit[i] == 0:
                if not dfs(i, path):
                    return []
        return path[::-1]

print Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print Solution().findOrder(2, [])