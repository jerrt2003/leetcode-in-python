class Solution(object):
    def insert(self, intervals, newInterval):
        """
        Facebook
        T:O(nlog(n)) S:O(n)
        Runtime: 60 ms, faster than 93.26% of Python online submissions for Insert Interval.
        Memory Usage: 16.2 MB, less than 26.11% of Python online submissions for Insert Interval.
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x: x[0])
        #
        # ans = []
        # for s, e in intervals:
        #     if not ans or s > ans[-1][1]:
        #         ans.append([s, e])
        #         continue
        #     if e < ans[-1][1]:
        #         continue
        #     pre_s, pre_e = ans.pop()
        #     ans.append([pre_s, e])
        #
        # return ans
        s, e = newInterval[0], newInterval[1]
        i = 0
        ans = []

        while i < len(intervals):
            curr_s, curr_e = intervals[i][0], intervals[i][1]
            if s <= curr_e:
                if e < curr_s:
                    break
                s = min(s, curr_s)
                e = max(e, curr_e)
            else:
                ans.append(intervals[i])
            i += 1

        ans.append([s, e])
        ans += intervals[i:]

        return ans