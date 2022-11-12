# -*- coding: utf-8 -*-
class Solution(object):
    def countSubstrings(self, s):
        """
        Solution: Center Expansion
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/palindromic-substrings/discuss/105687/Python-Straightforward-with-Explanation-(Bonus-O(N)-solution)
        Perf: Runtime: 72 ms, faster than 94.77% / Memory Usage: 10.9 MB, less than 26.68%
        :type s: str
        :rtype: int
        """
        m = len(s)
        res = 0
        for i in range(2*m-1):
            left = i/2
            right = i/2 + i%2
            while left >= 0 and right < m:
                if s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
                else:
                    break
        return res