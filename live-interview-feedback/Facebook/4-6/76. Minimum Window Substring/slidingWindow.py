import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        Sol: sliding window
        Time: O(s+t)
        Space: O(s+t)
        Perf: Runtime: 120 ms, faster than 59.86% / Memory Usage: 12.5 MB, less than 75.64%
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = collections.Counter(t)
        bkt = collections.defaultdict(int)
        pt1 = pt2 = formed = 0
        min_len = float('inf')
        res = ''
        while pt2 < len(s):
            bkt[s[pt2]] += 1
            if s[pt2] in counter and bkt[s[pt2]] == counter[s[pt2]]:
                formed += 1
            while pt1 <= pt2 and formed == len(counter):
                if pt2 - pt1 + 1 < min_len:
                    res = s[pt1:pt2 + 1]
                    min_len = pt2 - pt1 + 1
                bkt[s[pt1]] -= 1
                if s[pt1] in counter and bkt[s[pt1]] < counter[s[pt1]]:
                    formed -= 1
                pt1 += 1
            pt2 += 1
        return res

