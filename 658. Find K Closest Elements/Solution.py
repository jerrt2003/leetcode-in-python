# -*- coding: utf-8 -*-
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if k == 0:
            return []

        def findClosestIndx(arr, x):
            l, r = 0, len(arr)
            while l < r:
                m = (l+r-1)/2
                if arr[m] == x:
                    return m
                elif x > arr[m]:
                    l = m+1
                else:
                    r = m
            return l

        if x < arr[0]:
            start_idx = 0
        elif x > arr[-1]:
            start_idx = len(arr)-1
        else:
            start_idx = findClosestIndx(arr, x)
        low = max(0, start_idx - (k-1))
        high = min(len(arr)-1, start_idx + (k-1))

        while len(arr[low:high+1]) > k:
            if low == 0 or (abs(arr[low]-x) <= abs(arr[high]-x)):
                high -= 1
            elif high == len(arr)-1 or (abs(arr[low]-x) > abs(arr[high]-x)):
                low += 1
        return arr[low:high+1]

#arr = [1,2,3,4,5]
#arr = [1, 5, 7, 8, 12, 17, 20, 21]
#k = 4
#x = 3

#arr=[0,1,1,1,2,3,6,7,8,9]
#k=9
#x=4

#arr=[1]
#k=1
#x=0

#arr = [0,1,2,2,2,3,6,8,8,9]
#k = 5
#x = 9


arr = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5


print Solution().findClosestElements(arr, k, x)


