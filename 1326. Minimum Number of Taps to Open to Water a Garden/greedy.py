class Solution(object):
    def minTaps(self, n, ranges):
        """
        Greedy, similar to 1024
        T:O(nlogn) S:O(n)
        Runtime: 116 ms, faster than 83.53% of Python online submissions for Minimum Number of Taps to Open to Water a Garden.
        Memory Usage: 14.2 MB, less than 100.00% of Python online submissions for Minimum Number of Taps to Open to Water a Garden.
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        sections = []
        for idx, range in enumerate(ranges):
            sections.append([max(0, idx-range), idx+range])
        ans = 0
        curr_end, max_end = -1, 0
        for i, j in sorted(sections):
            if max_end >= n or i > max_end:
                break
            if curr_end < i <= max_end:
                ans += 1
                curr_end = max_end
            max_end = max(j, max_end)
        return ans if max_end >= n else -1