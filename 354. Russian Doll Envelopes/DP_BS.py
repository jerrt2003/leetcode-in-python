    # -*- coding: utf-8 -*-
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        Solution: DP+BS
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        Perf: Runtime: 68 ms, faster than 74.58% / Memory Usage: 12.5 MB, less than 46.15%
        Inspired By:
        - A time complexity improved version based on simple DP solution
        - https://segmentfault.com/a/1190000003819886#articleHeader1
        - https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
        - https://yanjia.me/zh/2018/11/05/70/
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if envelopes is None or len(envelopes) == 0 or len(envelopes[0]) < 2: return 0

        def getKey(elem):
            return elem[0], -elem[1]

        def getIndex(DP, l, r, target):
            while l < r:
                m = (l+r)/2
                if target > DP[m]:
                    l = m+1
                else:
                    r = m
            return l

        envelopes.sort(key=getKey)
        len_envelopes = len(envelopes)
        DP = [0 for _ in range(len_envelopes+1)]
        DP[0] = envelopes[0][1]
        max_len = 1
        for i in range(1, len_envelopes):
            if envelopes[i][1] < DP[0]:
                DP[0] = envelopes[i][1]
            elif envelopes[i][1] > DP[max_len-1]:
                DP[max_len] = envelopes[i][1]
                max_len += 1
            else:
                DP[getIndex(DP, 0, max_len-1, envelopes[i][1])] = envelopes[i][1]
        return max_len

#envelopes = [[5,4],[6,4],[6,7],[2,3]]
#envelopes = [[]]
envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]
print Solution().maxEnvelopes(envelopes)