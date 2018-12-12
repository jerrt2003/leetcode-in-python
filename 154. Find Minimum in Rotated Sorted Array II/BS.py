# -*- coding: utf-8 -*-
class Solution(object):
    def findMin(self, nums):
        """
        Solution: BS
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        Inspired By: MySELF!!
        TP:
        - with duplicate exists, we might hit situation where nums[mid] == nums[right]
            - then we don't know which side to "cut"
        - to solve that we can subtract 1 from 'r'
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            if l == r:
                return nums[l]
            mid = (l+r)/2
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1

#a = [2,2,2,0,1]
a = [1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1]
print Solution().findMin(a)