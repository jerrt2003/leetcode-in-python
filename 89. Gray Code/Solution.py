# -*- coding: utf-8 -*-
class Solution(object):
    def grayCode(self, n):
        """
        Solution: not sure..
        Time Complexity: O(nlog(n))
        Space Complexity: O(2^n)
        Inspired By: https://leetcode.com/problems/gray-code/discuss/29893/One-liner-Python-solution-(with-demo-in-comments)
        TP:
        ex. consider n = 3 scenario, gray code will be:
        [0,0,0]
        [0,0,1]
        [0,1,1] --> starting from here is 2^1 + reversed(前兩個result)
        [0,1,0]
        [1,1,0] --> starting from here is 2^2 + reversed(前四個result)
        [1,1,1]
        [1,0,1]
        [1,0,0]
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            res += [x + pow(2, i) for x in reversed(res)]
        return res

n = 0
print Solution().grayCode(n)