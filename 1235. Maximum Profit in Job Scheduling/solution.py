class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        DP+BS
        T:O(nlogn) S:O(n)
        Runtime: 672 ms, faster than 39.64% of Python online submissions for Maximum Profit in Job Scheduling.
        Memory Usage: 26.3 MB, less than 78.18% of Python online submissions for Maximum Profit in Job Scheduling.
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        lst = sorted(zip(startTime,endTime,profit), key=lambda x: x[1])
        DP = [(0, 0)]

        def bs(k):
            l, r = 0, len(DP)
            while l < r:
                mid = (l+r-1)/2
                if DP[mid][0] > k:
                    r = mid
                else:
                    l = mid+1
            return l-1

        for s, e, p in lst:
            i = bs(s)
            if p + DP[i][1] > DP[-1][1]:
                DP.append((e, p+DP[i][1]))

        return DP[-1][1]