# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        BS
        T:O(logn) S:O(1)
        Runtime: 40 ms, faster than 74.88% of Python online submissions for Find in Mountain Array.
        Memory Usage: 13.4 MB, less than 100.00% of Python online submissions for Find in Mountain Array.
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        # find the mountain
        l, r = 0, mountain_arr.length()
        while l < r:
            m = (l+r-1)//2
            if mountain_arr.get(m) > mountain_arr.get(m+1):
                r = m
            else:
                l = m+1
        mountain = l
        # find target at left-side of mountain
        l, r = 0, mountain
        while l < r:
            m = (l+r-1)//2
            if mountain_arr.get(m) == target:
                return m
            if mountain_arr.get(m) > target:
                r = m
            else:
                l = m+1
        # find target at right-side of mountain
        l, r = mountain, mountain_arr.length()
        while l < r:
            m = (l+r)//2
            if mountain_arr.get(m) == target:
                return m
            elif mountain_arr.get(m) < target:
                r = m
            else:
                l = m+1
        return -1