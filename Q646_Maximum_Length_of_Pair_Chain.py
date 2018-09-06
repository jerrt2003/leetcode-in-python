class Solution(object):
    def findLongestChain(self, pairs):
        """
        DP Solution
        :param pairs:
        :return:
        """
        pairs.sort()
        DP = [1]*len(pairs)
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    DP[i] = max(DP[i], DP[j]+1)
        return max(DP)


input = [[1,2], [3,4], [2,3], [7,9], [4,6]]
sol = Solution()
print sol.findLongestChain(input)