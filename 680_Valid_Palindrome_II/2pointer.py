# -*- coding: utf-8 -*-
class Solution(object):
    def validPalindrome(self, s):
        """
        Sol: 2pointer
        Perf: Runtime: 76 ms, faster than 88.54% / Memory Usage: 13 MB, less than 11.11%
        T: O(n)
        S: O(4n)
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        if l >= r:
            return True
        else:
            return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]