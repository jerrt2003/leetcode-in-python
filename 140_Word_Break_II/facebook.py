import collections


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Facebook
        T:O(n^2) S:O(n^2)
        Runtime: 32 ms, faster than 81.48% of Python online submissions for Word Break II.
        Memory Usage: 13.2 MB, less than 26.56% of Python online submissions for Word Break II.
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        DP = collections.defaultdict(list)
        breakable = [0] * len(s)

        def isBreakable(i):
            if i == len(s):
                return True
            if breakable[i] == 1:
                return True
            elif breakable[i] == -1:
                return False
            else:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict and isBreakable(j):
                        breakable[i] = 1
                        return breakable[i]
                breakable[i] = -1
                return breakable[i]

        def dfs(i):
            if i == len(s):
                return ['']
            if i in DP:
                return DP[i]
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict and isBreakable(j):
                    if i == 0:
                        DP[i] += [s[i:j] + a for a in dfs(j)]
                    else:
                        DP[i] += [" " + s[i:j] + a for a in dfs(j)]
            return DP[i]

        return dfs(0)