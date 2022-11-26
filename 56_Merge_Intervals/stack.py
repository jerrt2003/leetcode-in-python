from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if len(ans) == 0: # stack is empty
                ans.append(interval)
            else:
                prev_start, prev_end = ans[-1][0], ans[-1][1]
                start, end = interval[0], interval[1]
                if end <= prev_end:
                    continue
                elif start <= prev_end:
                    ans[-1][1] = end
                else:
                    ans.append(interval)
        return ans
