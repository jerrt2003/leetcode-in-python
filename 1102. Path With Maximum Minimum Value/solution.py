# class Solution(object):
#     def maximumMinimumPath(self, A):
#         """
#         T:O(4^mn) S:O(1)
#         TLE
#         :type A: List[List[int]]
#         :rtype: int
#         """
#         self.max_score = -float('inf')
#         m,n = len(A), len(A[0])
#         def dfs(i, j, path):
#             if i == m-1 and j == n-1:
#                 self.max_score = max(self.max_score, min([A[x][y] for x, y in path]))
#                 return
#             for x, y in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
#                 if 0<=x<m and 0<=y<n and (x, y) not in path:
#                     path.add((x, y))
#                     dfs(x, y, path)
#                     path.remove((x, y))
#
#         dfs(0, 0, set([(0, 0)]))
#
#         return self.max_score

class Solution(object):
    def maximumMinimumPath(self, A):
        """
        T:O(mnlog(mn)) S:O(mn)
        Runtime: 5860 ms, faster than 5.02% of Python online submissions for Path With Maximum Minimum Value.
        Memory Usage: 23.3 MB, less than 6.96% of Python online submissions for Path With Maximum Minimum Value.
        :type A: List[List[int]]
        :rtype: int
        """
        l, r = float('inf'), -float('inf')
        for row in A:
            for num in row:
                l = min(l, num)
                r = max(r, num)
        m, n = len(A), len(A[0])
        def isValid(K, i, j, grid):
            if i == m-1 and j == n-1 and A[i][j] >= K:
                return True
            if A[i][j] < K:
                return False
            grid[i][j] = 1
            for x, y in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
                if 0<=x<m and 0<=y<n and grid[x][y] != 1:
                    if isValid(K, x, y, grid):
                        return True
                    # path.remove((x, y))
            return False
        r += 1
        while l < r:
            mid = (l+r-1)/2
            grid = [[0 for _ in range(n)] for _ in range(m)]
            if not isValid(mid, 0, 0, grid):
                r = mid
            else:
                l = mid+1
        return l-1




print Solution().maximumMinimumPath([[5,4,5],[1,2,6],[7,4,6]])
print Solution().maximumMinimumPath([[2,2,1,2,2,2],[1,2,2,2,1,2]])
print Solution().maximumMinimumPath([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]])
print Solution().maximumMinimumPath([[1,1,0,3,1,1],[0,1,0,1,1,0],[3,3,1,3,1,1],[0,3,2,2,0,0],[1,0,1,2,3,0]])
print Solution().maximumMinimumPath([[0,1,0,0,0,1],[0,1,1,0,0,0],[0,0,1,1,0,1],[0,1,1,1,1,0],[1,1,1,1,1,1]])