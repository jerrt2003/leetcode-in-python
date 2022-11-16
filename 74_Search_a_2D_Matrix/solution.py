class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Facebook
        T:O(log(n)) S:O(1)
        Runtime: 52 ms, faster than 80.97% of Python online submissions for Search a 2D Matrix.
        Memory Usage: 14.5 MB, less than 53.25% of Python online submissions for Search a 2D Matrix.
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        l, r = 0, len(matrix)
        while l < r:
            m = (l+r-1)/2
            if matrix[m][0] > target:
                r = m
            else:
                l = m+1
        if l == len(matrix):
            return False
        row = matrix[l-1]
        l, r = 0, len(matrix[0])
        while l < r:
            m = (l+r-1)/2
            if row[m] >= target:
                r = m
            else:
                l = m+1
        if l == len(matrix[0]):
            return False
        return row[l] == target