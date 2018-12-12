# -*- coding: utf-8 -*-
class Solution(object):
    def search(self, nums, target):
        """
        Solution: Binary Search
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        Inspired By:
        - https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms
        - http://www.cnblogs.com/grandyang/p/4325648.html
        TP:
            - Possible rotating scenario:
            0　　1　　2　　4　　5　　6　　7
            7　　0　　1　　2　　4　　5　　6
            6　　7　　0　　1　　2　　4　　5
            5　　6　　7　　0　　1　　2　　4
            4　　5　　6　　7　　0　　1　　2
            2　　4　　5　　6　　7　　0　　1
            1　　2　　4　　5　　6　　7　　0
            - 觀察一下:
                -假設中位點nums[(left+right)/2] < nums[right] -> 中位點右側為sorted
                -反之若中位點nums[(left+right)/2] > nums[right] -> 中位點左側為sorted
            - 既然找的到sorted,則我們可以藉由判斷target是否在sorted那側來決定繼續用哪一側搜尋
            - 其餘的就是傳統的BS
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
        return -1