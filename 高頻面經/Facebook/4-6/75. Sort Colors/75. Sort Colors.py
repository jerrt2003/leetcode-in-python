# -*- coding: utf-8 -*-
class Solution(object):
    def sortColors(self, nums):
        """
        Sol: counting sort
        Time: O(n)
        Space: O(1)
        Ref: http://tinyurl.com/yxuunkmc
        Perf: Runtime: 20 ms, faster than 95.72% / Memory Usage: 12 MB, less than 5.30%
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        pt0, pt1, pt2 = 0, 0, len(nums)-1
        while pt1 <= pt2:
            if nums[pt1] == 0:
                nums[pt0], nums[pt1] = nums[pt1], nums[pt0]
                pt0 += 1
                pt1 += 1
            elif nums[pt1] == 1:
                pt1 += 1
            else:
                nums[pt1], nums[pt2] = nums[pt2], nums[pt1]
                pt2 -= 1
        return nums
        '''
        pt0, pt1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 2
                nums[pt1] = 1
                nums[pt0] = 0
                pt0+=1
                pt1+=1
            elif nums[i] == 1:
                nums[i] = 2
                nums[pt1] = 1
                pt1 += 1
        return nums

assert Solution().sortColors([2,0,2,1,1,0]) == [0,0,1,1,2,2]
#assert Solution().sortColors([1,0,2]) == [0,1,2]
#assert Solution().sortColors([0,2,1]) == [0,1,2]
#assert Solution().sortColors([2,1,0]) == [0,1,2]
#assert Solution().sortColors([1,1,0]) == [0,1,1]