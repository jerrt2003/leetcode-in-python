import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # hashmap to record curr substring
        curr_substring_counter = collections.defaultdict(int)

        # boudary variable
        l, r = 0, 0

        # ans var
        ans = 0

        while r < len(s):
            curr_substring_counter[s[r]] += 1
            while len(curr_substring_counter) > k:
                curr_substring_counter[s[l]] -= 1
                if curr_substring_counter[s[l]] == 0:
                    del curr_substring_counter[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
            r += 1

        return ans
