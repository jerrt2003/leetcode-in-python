# -*- coding: utf-8 -*-
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        Solution: Hash
        Time Complexity: O(m+n)
        Space Complexity: O(m+n)
        Inspired By: MySELF!!
        Ans to Follow up question:
        - 1. What if the given array is already sorted? How would you optimize your algorithm?
            - read each element from one of the list and use that element to BS against other list
            - Time complexity: O(m*log(n))
        - 2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
            - the m*log(n) is better
        - 3. What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
            - we can read one element at time for nums2 to get result
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        _tmp = dict()
        for num in nums1:
            if num in _tmp:
                _tmp[num] += 1
            else:
                _tmp[num] = 1
        res = []
        for num in nums2:
            if num in _tmp and _tmp[num] > 0:
                res.append(num)
                _tmp[num] -= 1
        return res

#nums1 = [1,2,2,1]
#nums2 = [2,2]

#nums1 = [4,9,5]
#nums2 = [9,4,9,8,4]

nums1 = []
nums2 = []



print Solution().intersect(nums1, nums2)