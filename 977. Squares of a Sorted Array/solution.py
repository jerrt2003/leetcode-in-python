class Solution(object):
    def sortedSquares(self, A):
        """
        2-pointer
        T:O(n) S:O(n)
        Runtime: 284 ms, faster than 12.65% of Python online submissions for Squares of a Sorted Array.
        Memory Usage: 14.7 MB, less than 5.13% of Python online submissions for Squares of a Sorted Array.
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A)-1
        res = []
        while i <= j:
            x, y = A[i], A[j]
            if abs(x) > abs(y):
                res.append(x*x)
                i += 1
            else:
                res.append(y*y)
                j -= 1
        return res[::-1]

print Solution().sortedSquares([-7,-3,2,3,11])