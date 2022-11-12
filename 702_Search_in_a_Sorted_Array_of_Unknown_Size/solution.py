# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        BS
        T:O(log(10000)) S:O(1)
        Runtime: 20 ms, faster than 87.91% of Python online submissions for Search in a Sorted Array of Unknown Size.
        Memory Usage: 13.2 MB, less than 89.86% of Python online submissions for Search in a Sorted Array of Unknown Size.
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l, r = 0, 10001
        while l < r:
            mid = (l+r-1)/2
            var = reader.get(mid)
            if var == target:
                return mid
            if var < target:
                l = mid+1
            elif var == 2147483647 or var > target:
                r = mid
        return -1