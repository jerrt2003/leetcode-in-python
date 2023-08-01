from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m
        while l < r:
            mid = (l + r - 1) // 2
            if matrix[mid][0] > target:
                r = mid
            else:
                l = mid + 1
        if l == 0:
            return False

        row = l - 1

        l, r = 0, n
        while l < r:
            mid = (l + r - 1) // 2
            if matrix[row][mid] >= target:
                r = mid
            else:
                l = mid + 1
        if l == n:
            return False
        return matrix[row][l] == target
