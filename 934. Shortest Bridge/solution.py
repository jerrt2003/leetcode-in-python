class Solution(object):
    def shortestBridge(self, A):
        """
        DFS
        BFS
        T:O(mn) S:O(mn)
        Runtime: 376 ms, faster than 80.95% of Python online submissions for Shortest Bridge.
        Memory Usage: 16 MB, less than 26.42% of Python online submissions for Shortest Bridge.
        :type A: List[List[int]]
        :rtype: int
        """
        m,n = len(A), len(A[0])
        queue = []
        def dfs(i, j):
            A[i][j] = -1
            queue.append((i, j))
            for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= x < m and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)
        found = False
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break

        step = 0
        while queue:
            l = len(queue)
            for _ in range(l):
                i, j = queue.pop(0)
                for x, y in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
                    if 0 <= x < m and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif A[x][y] == 0:
                            A[x][y] = -1
                            queue.append((x, y))
            step += 1

print Solution().shortestBridge([[0,1,0],[0,0,0],[0,0,1]])
print Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])