# -*- coding: utf-8 -*-
class Solution(object):
    def findMaxHappines(self, groupList, busSize):
        """
        f[i][v] = max(f[i-1][v], f[i-1][v - groupSize[i]] + happy[i])
        :param groupList:
        :param busSize:
        :return:
        """
        m = len(groupList)
        n = busSize + 1
        dp = [0] * n
        for i in range(1, m):
            for j in range(n-1, len(groupList[i])-1, -1):
                x = j - len(groupList[i-1])
                dp[j] = max(dp[j], dp[j - len(groupList[i-1])] + self.happy(groupList[i-1]))
        return dp[-1]


    def happy(self, word):
        happyMap = {'c':4, 'w':3, 'm':2, 's':1}
        sum = 0
        for w in word:
            sum += happyMap[w]
        return sum * len(word)

group = ['msc','wmc','wwmc','sms']
bus = 10

assert Solution().findMaxHappines(group, bus)
