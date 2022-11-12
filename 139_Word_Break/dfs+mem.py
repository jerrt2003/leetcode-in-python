class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Facebook
        DFS
        DP-Mem
        Runtime: 32 ms, faster than 54.34% of Python online submissions for Word Break.
        Memory Usage: 13.1 MB, less than 14.46% of Python online submissions for Word Break.
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        DP = [0] * len(s)
        wordDict = set(wordDict)

        def dfs(i):
            if i == len(s):
                return True
            if DP[i] == 1:
                return False
            for j in range(i + 1, len(s)+1):
                if s[i:j] in wordDict:
                    if dfs(j):
                        return True
            DP[i] = 1
            return False

        return dfs(0)

print Solution().wordBreak("leetcode", ["leet","code"])
print Solution().wordBreak("applepenapple",["apple", "pen"])
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
sol = Solution()
print sol.wordBreak(s, wordDict)