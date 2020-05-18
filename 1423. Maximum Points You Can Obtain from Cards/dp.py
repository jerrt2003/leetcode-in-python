import collections


class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        recursive + memorization
        TLE
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if len(cardPoints) == 0: return 0
        self.dp = collections.defaultdict(int)
        return self.dfs(0, len(cardPoints)-1, cardPoints, k)

    def dfs(self, start, end, cardPoints, k):
        if start == end:
            return cardPoints[start]
        elif k == 1:
            return max(cardPoints[start], cardPoints[end])
        else:
            if self.dp[(start, end, k)] != 0:
                return self.dp[(start, end, k)]
            curr_max = max(cardPoints[start]+self.dfs(start+1, end, cardPoints, k-1), self.dfs(start, end-1, cardPoints, k-1)+cardPoints[end])
            self.dp[(start, end, k)] = curr_max
            return curr_max


print Solution().maxScore([1,2,3,4,5,6,1], 3)
print Solution().maxScore([2,2,2], 2)
print Solution().maxScore([9,7,7,9,7,7,9], 7)
print Solution().maxScore([1,1000,1], 1)
print Solution().maxScore([], 3)