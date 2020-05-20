import collections

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        T:O(n) S:O(n)
        Runtime: 132 ms, faster than 18.67% of Python online submissions for Element Appearing More Than 25% In Sorted Array.
        Memory Usage: 14.5 MB, less than 100.00% of Python online submissions for Element Appearing More Than 25% In Sorted Array.
        :type arr: List[int]
        :rtype: int
        """
        counter = collections.Counter(arr)
        for k, v in counter.iteritems():
            if v > len(arr)*0.25:
                return k
        return None