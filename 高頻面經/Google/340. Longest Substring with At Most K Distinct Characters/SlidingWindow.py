# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Solution: Sliding Window
        Perf: Runtime: 60 ms, faster than 77.60% / Memory Usage: 12.2 MB, less than 65.94%
        Time: O(n)
        Space: O(n)
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s: return 0
        res = -float('inf')
        bkt = hash2.defaultdict(int)
        pt1, pt2 = 0, 0
        while pt2 < len(s):
            bkt[s[pt2]] += 1
            while len(bkt) > k:
                bkt[s[pt1]] -= 1
                if bkt[s[pt1]] == 0:
                    del bkt[s[pt1]]
                pt1 += 1
            res = max(res, pt2-pt1+1)
            pt2 += 1
        return res

assert Solution().lengthOfLongestSubstringKDistinct('eceba',2) == 3
assert Solution().lengthOfLongestSubstringKDistinct('aa',1) == 2
assert Solution().lengthOfLongestSubstringKDistinct('aaabbbc',2) == 6
assert Solution().lengthOfLongestSubstringKDistinct('a',2) == 1