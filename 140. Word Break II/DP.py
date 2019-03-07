# -*- coding: utf-8 -*-
class Solution:
    def wordBreak(self, s, wordDict):
        """
        Solution: DP
        Time complexity:
        Space complexity:
        Inspired by:
        Algorithm:
        - Create a list DP with length: len(s)+1
        - Each of the DP element should be a list compose of all possible string
        - DP[0] is an empty string (since 0 word can be break into dict words)
        - Apply the same logic in Q139
        - if DP[j] is not empty and s[j:i] in wordDict then we add s[j:i] into all strings in DP[j],
        and DP[i] will equal to this new list
        - return DP[-1]
        - !!!!! the above forward tracking solution will hit MLE, thus we first check if string is breakable to
        avoid that !!!!!
        Perf: Runtime: 156 ms, faster than 9.01% / Memory Usage: 11 MB, less than 80.43%
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # First check if word is breakable to avoid MLE
        def breakable():
            rightmosts = [0]
            for i in range(1, len(s) + 1):
                for last_index in rightmosts:
                    if s[last_index:i] in wordDict:
                        rightmosts.append(i)
                        if i == len(s):
                            return True
                        break
            return False

        if breakable():
            # Following is the same logic
            DP_len = len(s)+1
            DP = [[] for _ in range(DP_len)]
            DP[0].append("")
            for i in range(1, DP_len):
                for j in range(i):
                    if len(DP[j]) != 0 and s[j:i] in wordDict:
                        tmp_word = s[j:i]
                        for word_string in DP[j]:
                            if len(word_string) == 0:
                                new_word = tmp_word
                            else:
                                new_word = word_string + " " + tmp_word
                            DP[i].append(new_word)
            return DP[-1]
        else:
            return []

#s = "catsanddog"
#wordDict = ["cat", "cats", "and", "sand", "dog"]

#s = "pineapplepenapple"
#wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

sol = Solution()
print sol.wordBreak(s, wordDict)
