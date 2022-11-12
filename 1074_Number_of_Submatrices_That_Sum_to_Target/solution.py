import collections


class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        T:O(mn^2) S:O(mn)
        Runtime: 6588 ms, faster than 23.12% of Python online submissions for Number of Submatrices That Sum to Target.
        Memory Usage: 19.1 MB, less than 100.00% of Python online submissions for Number of Submatrices That Sum to Target.
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(n-1):
                row[i+1] += row[i]
        res = 0
        for i in range(n):
            for j in range(i, n):
                cur = 0
                sum_occur = collections.defaultdict(int)
                sum_occur[0] = 1
                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i-1] if i > 0 else 0)
                    res += sum_occur[cur - target]
                    sum_occur[cur] += 1
        return res





# print Solution().numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0)
print Solution().numSubmatrixSumTarget([[1,-1],[-1,1]], 0)