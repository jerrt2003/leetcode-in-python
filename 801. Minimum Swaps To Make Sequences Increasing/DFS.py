# -*- coding: utf-8 -*-
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        self.min_swap = float('inf')
        self.dfs(A, B, 1, 0)
        return self.min_swap

    def dfs(self, A, B, i, curr_swap):
        if curr_swap >= self.min_swap:
            return
        if i == len(A):
            self.min_swap = min(self.min_swap, curr_swap)
            return
        if A[i] > A[i-1] and B[i] > B[i-1]:
            self.dfs(A, B, i+1, curr_swap)
        elif A[i] > B[i-1] and B[i] > A[i-1]:
            A[i], B[i] = B[i], A[i]
            self.dfs(A, B, i+1, curr_swap+1)
            A[i], B[i] = B[i], A[i]



A = [1,3,5,4]
B = [1,2,3,7]

print Solution().minSwap(A, B)