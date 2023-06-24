from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not ans:
                ans.append(interval)
            else:
                prev_s, prev_e = ans[-1][0], ans[-1][1]
                curr_s, curr_e = interval[0], interval[1]

                if curr_s > prev_e:
                    ans.append(interval)
                else:
                    ans.pop()
                    ans.append([min(prev_s, curr_s), max(prev_e, curr_e)])

        return ans
