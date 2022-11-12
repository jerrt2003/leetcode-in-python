# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        Facebook
        T:O(mlog(n)) S:O(1)
        Runtime: 88 ms, faster than 86.21% of Python online submissions for Leftmost Column with at Least a One.
        Memory Usage: 13.1 MB, less than 28.93% of Python online submissions for Leftmost Column with at Least a One.
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        m, n = binaryMatrix.dimensions()
        ans = float('inf')
        left_most = n - 1
        for i in range(m):
            if binaryMatrix.get(i, left_most) == 0:
                continue
            l, r = 0, left_most + 1
            while l < r:
                mid = (l + r - 1) / 2
                if binaryMatrix.get(i, mid) >= 1:
                    r = mid
                else:
                    l = mid + 1
            if l != n:
                left_most = l
                ans = min(ans, left_most)
        return -1 if ans == float('inf') else ans