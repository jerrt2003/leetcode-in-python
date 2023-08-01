from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] > target:
                return False
            l, r = 0, n
            while l < r:
                mid = (l + r - 1) // 2
                if matrix[i][mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            # 若 l == n，出界，表示找不到target，續往下一列找
            if l == n:
                continue
            if matrix[i][l] == target:
                return True
        return False
