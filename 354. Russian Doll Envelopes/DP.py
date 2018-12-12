# -*- coding: utf-8 -*-
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        Solution: DP (TLE)
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        Inspired By:
        - https://leetcode.com/problems/russian-doll-envelopes/discuss/82763/Java-NLogN-Solution-with-Explanation
        - https://leetcode.com/problems/longest-increasing-subsequence/solution/
        TP:
        - envelope: [width, height]
        - Sort the envelopes based on width (ascending order) and height(descending order)
            - ex. [[5,4],[6,4],[6,7],[2,3]] --> [[2,3],[5,4],[6,7],[6,4]]
        - Since width is already in ascending order, we just need to find maximum ascending order based on height to find answer
            - remember, we already sort height in descending order so we can guarantee the answer is correct
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def getkey(elem):
            return elem[0],-elem[1]

        if envelopes is None or len(envelopes) == 0 or len(envelopes[0])<2: return 0

        envelopes.sort(key=getkey)
        total_len = len(envelopes)
        DP = [0 for _ in range(total_len)]
        for i in range(total_len):
            _max = 0
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    _max = max(_max, DP[j])
            DP[i] = _max+1
        return max(DP)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
#envelopes = [[]]
print Solution().maxEnvelopes(envelopes)