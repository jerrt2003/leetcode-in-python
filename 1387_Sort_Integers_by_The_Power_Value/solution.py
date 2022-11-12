import collections


class Solution(object):
    def getKth(self, lo, hi, k):
        """
        DP: memorization
        T:O(nlog(n)) S:O(n)
        Runtime: 188 ms, faster than 76.25% of Python online submissions for Sort Integers by The Power Value.
        Memory Usage: 36.9 MB, less than 100.00% of Python online submissions for Sort Integers by The Power Value.
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        DP = collections.defaultdict(int)

        def dfs(x):
            if x in DP:
                return DP[x]
            if x == 1:
                return 0
            if x % 2 == 0:
                DP[x] = 1+dfs(x/2)
            else:
                DP[x] = 1+dfs(3*x+1)
            return DP[x]


        for x in range(lo, hi+1):
            DP[x] = dfs(x)
        arr = [x for x in range(lo, hi+1)]
        arr.sort(key=lambda x: DP[x]) # sorting is nlog(n)
        return arr[k-1]

print Solution().getKth(1, 1000, 777)