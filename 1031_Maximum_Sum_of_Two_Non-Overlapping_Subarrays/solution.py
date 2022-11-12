class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        prefix sum
        T:O(n) S:O(1)
        Runtime: 32 ms, faster than 93.93% of Python online submissions for Maximum Sum of Two Non-Overlapping Subarrays.
        Memory Usage: 12.8 MB, less than 54.60% of Python online submissions for Maximum Sum of Two Non-Overlapping Subarrays.
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        for i in range(1, len(A)):
            A[i] += A[i-1]
        res = A[L+M-1]
        L_max = A[L-1]
        M_max = A[M-1]
        for i in range(L+M, len(A)):
            L_max = max(L_max, A[i-M]-A[i-M-L])
            M_max = max(M_max, A[i-L]-A[i-L-M])
            res = max(res, L_max+A[i]-A[i-M], M_max+A[i]-A[i-L])
        return res