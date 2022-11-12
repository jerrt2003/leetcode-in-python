# -*- coding: utf-8 -*-
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Solution: BS
        Time Complexity: O(2log(n)) --> 24ms
        Space Complexity: O(1)
        Inspired By: MySELF!!
        TP:
        - using each row's head value to determine which row the target "might" possibly located
        - once found row, do a 2nd BS to determine if the number existed or not
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix)==0:
            return False
        if matrix[0] is None or len(matrix[0]) == 0:
            return False

        def find_in_row(nums, target):
            l = 0
            r = len(nums)-1
            while l <= r:
                m = (l+r)/2
                if nums[m] == target:
                    return True
                elif nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return False

        l = 0
        r = len(matrix)-1
        while l <= r:
            m = (l+r)/2
            start = matrix[m][0]
            end = matrix[m][len(matrix[0])-1]
            if start <= target <= end:
                return find_in_row(matrix[m], target)
            elif target < start:
                r = m-1
            else:
                l = m+1
        return False

'''
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
'''
matrix = []

target = 0

print Solution().searchMatrix(matrix, target)