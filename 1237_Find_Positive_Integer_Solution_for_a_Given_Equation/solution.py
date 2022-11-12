"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""


class Solution(object):
    def findSolution(self, customfunction, z):
        """
        2 dimension BS
        T:O(2*log(n)), S:O(n)
        Runtime: 16 ms, faster than 98.63% of Python online submissions for Find Positive Integer Solution for a Given Equation.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Find Positive Integer Solution for a Given Equation.
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        res = []
        for x in range(1, z+1):
            l, r = 1, z+1
            while l < r:
                m = (l+r-1)/2
                if customfunction.f(x, m) == z:
                    res.append([x, m])
                    break
                elif customfunction.f(x, m) > z:
                    r = m
                else:
                    l = m+1
        return res