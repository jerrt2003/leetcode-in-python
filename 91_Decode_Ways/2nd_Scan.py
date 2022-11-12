# -*- coding: utf-8 -*-
class Solution(object):
    def numDecodings(self, s):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(1)
        Perf: Runtime: 24 ms, faster than 92.33% / Memory Usage: 10.8 MB, less than 38.95%
        Inspired By: https://leetcode.com/problems/decode-ways/discuss/30592/DP-solution-with-detailed-explanation-Python-sample-code
        :type s: str
        :rtype: int
        """
        if not s or s == '0':
            return 0
        m = len(s)
        care, dont = 0, 1
        for i in range(1, m):
            p, c = s[i-1], s[i]
            if c == '0':
                if p != '1' and p != '2':
                    return 0 # fail to decode
                else:
                    care, dont = dont, 0 # decode with '10' or '20' means p is not used in previous decode so care, dont = dont, 0
            elif p == '0':
                care, dont = 0, care # means p must be decode with its predecessor thus care, dont = 0, care
            else:
                if 11 <= int(p+c) <= 26:
                    care, dont = dont, dont + care
                else:
                    care, dont = 0, dont + care
        return care + dont

s = '10'
print Solution().numDecodings(s)