class Solution(object):
    '''
    def wordBreak(self, s, wordDict):
        """
        Recursion (TLE)
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def findWordBreak(s, wordDict, str):
            for w in wordDict:
                sub_len = len(str+w)
                target_len = len(s)
                if sub_len > target_len:
                    continue
                elif sub_len < target_len:
                    if s[:sub_len] == str+w:
                        if findWordBreak(s, wordDict, str+w):
                            return True
                else:
                    if str+w == s:
                        return True
            return False

        return findWordBreak(s, wordDict, '')
    '''

    def wordBreak(self, s, wordDict):
        """
        DP solution: https://leetcode.com/problems/word-break/discuss/43790/Java-implementation-using-DP-in-two-ways
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        :param s:
        :param wordDict:
        :return: bool
        """
        DP = [False]*(len(s)+1) #DP[i] means words 0 to i-1 can be break into dict word
        DP[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if DP[j] and s[j:i] in wordDict:
                    DP[i] = True
                    break
        return DP[len(s)]

#s = "leetcode"
#wordDict = ["leet", "code"]

#s = "applepenapple"
#wordDict = ["apple", "pen"]

#s = "catsandog"
#wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "abcd"
wordDict = ["c","abc","b","cd"]

sol = Solution()
print sol.wordBreak(s, wordDict)
