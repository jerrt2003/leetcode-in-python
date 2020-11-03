class Solution(object):
    def shortestPath(self, grid, k):
        """
        T:O(mnk) S:O(mnk)
        Runtime: 92 ms, faster than 64.08% of Python online submissions for Shortest Path in a Grid with Obstacles Elimination.
        Memory Usage: 14.1 MB, less than 53.45% of Python online submissions for Shortest Path in a Grid with Obstacles Elimination.
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if k > (m-1)+(n-1):
            return (m-1)+(n-1)

        q = [(0, 0, 0, k)]
        visit = set([(0, 0, k)])

        while q:
            l = len(q)
            new_q = []
            for _ in range(l):
                i, j, step, k = q.pop(0)
                if i == m-1 and j == n-1:
                    return step
                for x, y in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
                    if 0<=x<m and 0<=y<n:
                        if grid[x][y] == 1 and k > 0 and (x, y, k-1) not in visit:
                            visit.add((x, y, k-1))
                            new_q.append((x, y, step+1, k-1))
                        elif grid[x][y] == 0 and (x, y, k) not in visit:
                            visit.add((x, y, k))
                            new_q.append((x, y, step+1, k))
            q = new_q
        return -1

print Solution().shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1)
print Solution().shortestPath([[0,1,1],[1,1,1],[1,0,0]],1)
print Solution().shortestPath([[0,0,1,0,0],[0,1,0,1,0]],2)