# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        Solution: Sliding Window + 2 pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        Perf: Runtime: 48 ms, faster than 54.27% / Memory Usage: 11.9 MB, less than 30.77%
        Inspired By: MySELF!!
        :type s: str
        :rtype: int
        """
        if not s: return 0
        if len(s) == 1: return 1
        bucket = hash2.defaultdict(int)
        pt1, pt2 = 0, 1
        bucket[s[pt1]] += 1
        m = len(s)
        res = -float('inf')
        while pt2 < m:
            bucket[s[pt2]] += 1
            while len(bucket) > 2:
                bucket[s[pt1]] -= 1
                if bucket[s[pt1]] == 0:
                    del bucket[s[pt1]]
                pt1 += 1
            res = max(res, pt2 - pt1 + 1)
            pt2 += 1
        return res

