import collections


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Facebook
        Sliding Window
        T:O(n) S:O(n)
        Runtime: 64 ms, faster than 70.75% of Python online submissions for Longest Substring with At Most K Distinct Characters.
        Memory Usage: 14.8 MB, less than 13.93% of Python online submissions for Longest Substring with At Most K Distinct Characters.
        :type s: str
        :type k: int
        :rtype: int
        """
        words = collections.defaultdict(int)
        j = 0
        ans = -float('inf')
        for i in range(len(s)):
            words[s[i]] += 1
            if len(words) <= k:
                ans = max(ans, i - j + 1)
            while len(words) > k:
                words[s[j]] -= 1
                if words[s[j]] == 0:
                    del words[s[j]]
                j += 1
        return 0 if ans == -float('inf') else ans

print Solution().lengthOfLongestSubstringKDistinct("a", 2)