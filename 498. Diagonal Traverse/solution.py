import collections


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        Facebook
        T:O(mn) S:O(mn)
        Runtime: 272 ms, faster than 14.84% of Python online submissions for Diagonal Traverse.
        Memory Usage: 16.8 MB, less than 7.44% of Python online submissions for Diagonal Traverse.
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        group = collections.defaultdict(list)
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                group[i+j].append(matrix[i][j])
        ans = []
        for idx in range(m + n - 1):
            if idx % 2 == 0:
                ans += group[idx][::-1]
            else:
                ans += group[idx]

        return ans

print Solution().findDiagonalOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])
print Solution().findDiagonalOrder([[ 1, 2, 3 ]])