# -*- coding: utf-8 -*-
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        T: O(n)
        S: O(n)
        Perf: Runtime: 68 ms, faster than 58.64%  / Memory Usage: 12.1 MB, less than 39.53%
        ** Iterate through the array, each time all elements to the left are smaller (or equal) to all elements to the right, there is a new chunck
        :type arr: List[int]
        :rtype: int
        """
        max_left = [0] * len(arr)
        min_right = [0] * len(arr)

        max_left[0] = arr[0]
        for i in range(1, len(arr)):
            max_left[i] = max(max_left[i - 1], arr[i])

        min_right[len(arr) - 1] = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], arr[i])

        count = 0
        for i in range(len(arr) - 1):
            if max_left[i] <= min_right[i + 1]:
                count += 1

        return count + 1
