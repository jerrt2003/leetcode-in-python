# -*- coding: utf-8 -*-
import hash2

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        Solution: Hashset
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!(104ms, beat 66%)
        TP:
        - Using Hashset to log number's position and calculate the frequency
        :type nums: List[int]
        :rtype: int
        """
        degree = hash2.defaultdict(list)
        for i in range(len(nums)):
            degree[nums[i]].append(i)
        max_degree = -float('inf')
        for v in degree.values():
            max_degree = max(max_degree, len(v))
        res = float('inf')
        for v in degree.values():
            if len(v) < max_degree:
                continue
            else:
                res = min(res, v[max_degree-1] - v[0] + 1)
        return res

nums = [1, 2, 2, 3, 1]
print Solution().findShortestSubArray(nums)