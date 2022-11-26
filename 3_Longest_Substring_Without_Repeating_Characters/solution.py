import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a dict(hashmap) for quick character reference
        seen = collections.defaultdict(int)
        j, ans = 0, 0
        for i, c in enumerate(s):
            seen[c] += 1
            while seen[c] > 1: # why we need to use 'while' instead of `if` -> repeating character not necessary located at position j
                seen[s[j]] -= 1
                j += 1
            ans = max(ans, i-j+1)
        return ans
