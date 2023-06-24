from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                prev_s, prev_e = stack[-1][0], stack[-1][1]
                curr_s, curr_e = interval[0], interval[1]
                if curr_s >= prev_e:
                    stack.append(interval)
                else:
                    return False
        return True
