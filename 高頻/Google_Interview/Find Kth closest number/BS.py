# -*- coding: utf-8 -*-
class Solution(object):
    def findKthClosestElement(self, arr, K, C):
        l, r = 0, len(arr)
        while l < r:
            m = (l+r-1)/2
            if arr[m] >= K:
                r = m
            else:
                l = m+1
        if arr[l] == K:
            left = max(0, l - (C-1))
            right = min(len(arr), l + (C-1))
            C -= 1
        else:
            left = max(0, l-C)
            right = min(len(arr), l+(C-1))
        while C > 0:
            if abs(arr[left]-K) <= abs(arr[right]-K):
                right -= 1
            else:
                left += 1
            C -= 1
        if abs(arr[left]-K) >= abs(arr[right]-K):
            return arr[left]
        else:
            return arr[right]

arr = [1, 3, 5, 10, 20, 23]
K = 2
C= 2

print Solution().findKthClosestElement(arr, K, C)