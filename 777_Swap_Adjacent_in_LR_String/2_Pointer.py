# -*- coding: utf-8 -*-
class Solution(object):
    def canTransform(self, start, end):
        """
        Solution: 2-pointer, Invariant
        Time Complexity: O(n)
        Space Complexity: O(1)
        Perf: Runtime: 48 ms, faster than 71.94% / Memory Usage: 12.1 MB, less than 21.74%
        Inspired By: https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/250541/Python-2-pass-O(n)
        :type start: str
        :type end: str
        :rtype: bool
        """
        if start.replace('X','') != end.replace('X',''):
            return False
        m = len(start)

        def check(pt1, pt2, chr):
            while pt1 < m:
                if start[pt1] == chr:
                    while end[pt2] != chr:
                        pt2 += 1
                    if chr == 'R':
                        if not pt1 <= pt2:
                            return False
                    else:
                        if not pt1 >= pt2:
                            return False
                    pt2 += 1
                pt1 += 1
            return True

        return check(0,0,'R') and check(0,0,'L')

start = "RXXLRXRXL"
end = "XRLRXXRLX"
print Solution().canTransform(start, end)
