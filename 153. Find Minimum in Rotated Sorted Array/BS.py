# -*- coding: utf-8 -*-
class Solution(object):
    def findMin(self, nums):
        """
        Solution: BS
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        Inspired By:
        - https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution
        - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/
        TP:
        - mid = (left+right)/2
        - 假如nums[mid]>nums[right]:表示右側為rotated過的那一側,去那邊找最小數
        - 反之往另外一側找
        - Nov.14, 2018: 想想看這個例子 nums = [2,5,6,0,0,1,2] 為什麼也會work呢?
            - 第一次的mid = 0, 0 < 2, 所以rotate會在左側呦
        - Jan.9, 2019: 在每次的二分法中去unsorted的那側找最小數
          ex. [7,8,9,1,2,3] (kind like special case)
          --> after 1st BS, we'll continue to find [1,2,3]
          --> after 2nd BS, we'll continue to find [1,2]
          --> after 3rd BS, we'll continue to find [1]
          --> answer get
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            if left == right:
                return nums[left]
            mid = (left+right)/2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid # The way how BS works is to divide an list(or array) into 2 parts: [left,mid] and [mid+1, right], thus we use right = mid here

a = [3,4,5,1,2]
#a = [1,2,3,4,5]
sol = Solution()
print sol.findMin(a)
