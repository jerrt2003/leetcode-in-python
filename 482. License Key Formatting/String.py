# -*- coding: utf-8 -*-
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        Solution: String manipulation
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!! (88ms, beat 60.09%)
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []
        s = S.split('-')
        s = ''.join(s)
        sec = []
        for _s in s[::-1]:
            if len(sec) == K:
                res.append(''.join(sec[::-1]))
                sec = []
            if _s.isalpha():
                sec.append(_s.upper())
            elif _s.isdigit():
                sec.append(_s)
        res.append(''.join(sec[::-1])) # last one
        return '-'.join(res[::-1])

S = "2-5g-3-J"
K = 2
print Solution().licenseKeyFormatting(S, K)