# -*- coding: utf-8 -*-
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        Solution: O(n)
        Time Complexity: O(n)
        Space Complexity: O(1)
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1][1]
            curr_start = intervals[i][0]
            if prev_end > curr_start:
                return False
        return True
