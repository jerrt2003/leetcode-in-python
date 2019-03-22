# -*- coding: utf-8 -*-
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        Solution: O(n)
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        Perf: Runtime: 60 ms, faster than 67.65% / Memory Usage: 13.3 MB, less than 29.87%
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-','')
        res = []
        bucket = []
        for chr in S[::-1]:
            bucket.append(chr.upper())
            if len(bucket) == K:
                res.append(''.join(bucket[::-1]))
                bucket = []
        if bucket:
            res.append(''.join(bucket[::-1]))
        res = '-'.join(res[::-1])
        return res if not res.startswith('-') else res[1:]