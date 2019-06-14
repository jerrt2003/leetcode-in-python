# -*- coding: utf-8 -*-
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Solution: BS
        Time Complexity: O(log(n))
        Space Complexity:O (1)
        Perf: Runtime: 40 ms, faster than 60.79% / Memory Usage: 13.6 MB, less than 58.82%
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # find smallest m where target > matrix[m][-1]
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m
        while l < r:
            mid = (l + r - 1) // 2
            if target <= matrix[mid][-1]:
                r = mid
            else:
                l = mid + 1
        # search at row[l]
        row = matrix[-1] if l == m else matrix[l] #!!! 注意沒找到的情況
        l, r = 0, n
        while l < r:
            mid = (l + r - 1) / 2
            if row[mid] == target:
                return True
            if row[mid] > target:
                r = mid
            else:
                l = mid + 1
        return False

assert Solution().searchMatrix([[1,1]], 2) == False
assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13) == False