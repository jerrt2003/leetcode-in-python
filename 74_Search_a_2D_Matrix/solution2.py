from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check invalid condition
        if len(matrix[0]) == 0:
            return False
        # check which row the target could be in
        row = self._find_row(matrix, target)
        # check if target in that row
        return self._find_target(matrix[row], target)

    def _find_row(self, matrix: List[List[int]], target: int) -> int:
        head_indicies = []
        for m in matrix:
            head_indicies.append(m[0])
        l, r = 0, len(head_indicies)
        while l < r:
            m = (l+r-1)//2
            if head_indicies[m] > target:
                r = m
            else:
                l = m+1
        return l-1

    def _find_target(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)
        while l < r:
            m = (l+r-1)//2
            if nums[m] > target:
                r = m
            else:
                l = m+1
        return nums[l-1] == target