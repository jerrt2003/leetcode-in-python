# -*- coding: utf-8 -*-
class Solution(object):
    def findPermutation(self, s):
        """
        T: O(n)
        S: O(1)
        Perf: Runtime: 80 ms, faster than 80.00% / Memory Usage: 13.3 MB, less than 7.32%
        :type s: str
        :rtype: List[int]
        """
        res = [1+i for i in range(len(s)+1)]
        i = 0
        while i < len(s):
            if s[i] == 'D':
                j = i
                while j+1 < len(s):
                    if s[j+1] == 'D':
                        j += 1
                    else:
                        break
                l, r = i, j+1
                while l < r:
                    res[l], res[r] = res[r], res[l]
                    l += 1
                    r -= 1
                i = j
            i += 1
        return res


assert Solution().findPermutation("DDIIDI") == [3,2,1,4,6,5,7]
assert Solution().findPermutation("D") == [2,1]