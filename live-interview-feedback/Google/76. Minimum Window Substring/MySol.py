# -*- coding: utf-8 -*-
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        idx_dict = dict()
        for char in set(t):
            idx_dict[char] = float('inf')
        min_windows = float('inf')
        res = ''
        for i in range(len(s)):
            if s[i] in set(t):
                idx_dict[s[i]] = i
            if max(idx_dict.values()) - min(idx_dict.values()) < min_windows:
               res = s[min(idx_dict.values()):max(idx_dict.values())+1]
        return res

s = "ADOBECODEBANC"
t = "ABC"

print Solution().minWindow(s, t)