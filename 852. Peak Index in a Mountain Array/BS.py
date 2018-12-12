# -*- coding: utf-8 -*-
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        Solution: BS
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        TP:
        - Using BS to decide which side the peak value might located
        :type A: List[int]
        :rtype: int
        """
        if A is None or len(A) == 0: return None
        l = 0
        r = len(A)-1
        while l <= r:
            m = (l+r)/2
            if A[m] > A[m-1] and A[m] > A[m+1]:
                return m
            elif A[m] > A[m-1]:
                l = m+1
            else:
                r = m-1

#A = [0,1,0]
A = [3,4,5,1]
print Solution().peakIndexInMountainArray(A)
