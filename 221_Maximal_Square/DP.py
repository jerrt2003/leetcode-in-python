# -*- coding: utf-8 -*-
class Solution(object):
    def maximalSquare(self, matrix):
        """
        Solution: DP
        Time Complexity: O(m*n)
        Space Complexity: O(n)
        Perf: Runtime: 56 ms, faster than 99.91% / Memory Usage: 16.2 MB, less than 9.28%
        Inspired By: MySELF!! + https://leetcode.com/problems/maximal-square/discuss/61804/Python-80ms-DP-solution-beats-100-O(mn)-time-one-pass
        TP:
        - borrowed the idea of Q.84: largest rectangle in histogram
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        DP = [0 for _ in range(n)]
        max_size = 0
        for i in range(m):
            count = 0
            max_count = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    DP[j] += 1
                else:
                    DP[j] = 0
                if DP[j] > max_size:
                    count += 1
                    max_count = max(max_count, count)
                else:
                    count = 0
            if max_count > max_size:
                max_size += 1

        return max_size*max_size


matrix = [["1","0","0","1","1","0","1","1"],
          ["1","0","0","0","0","1","0","0"],
          ["0","1","1","1","0","0","1","1"],
          ["0","0","0","1","0","0","0","1"],
          ["0","0","0","0","0","1","1","1"],
          ["1","1","1","1","1","1","1","1"],
          ["1","0","0","1","0","1","1","0"],
          ["0","1","1","0","1","1","1","0"]]

print Solution().maximalSquare(matrix)
