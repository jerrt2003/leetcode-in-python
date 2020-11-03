import collections


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        knapsack01
        T:O(s*mn) S:O(mn) *s: len of strings
        Runtime: 3308 ms, faster than 41.92% of Python online submissions for Ones and Zeroes.
        Memory Usage: 13 MB, less than 56.21% of Python online submissions for Ones and Zeroes.
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        items = list()
        for s in strs:
            counter = collections.Counter(s)
            items.append([counter['0'],counter['1']])
        DP = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # DP[0][0] = 1 <-- no need because when m = 0 and n = 0, can't form any string
        for i in range(len(items)):
            for j in range(m, items[i][0]-1, -1):
                for k in range(n, items[i][1]-1, -1):
                    DP[j][k] = max(DP[j][k], DP[j-items[i][0]][k-items[i][1]]+1)
        return DP[-1][-1]


print Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3)
print Solution().findMaxForm(["10","1","0"], 1, 1)