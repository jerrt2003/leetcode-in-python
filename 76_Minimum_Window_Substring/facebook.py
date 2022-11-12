import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 104 ms, faster than 77.46% of Python online submissions for Minimum Window Substring.
        Memory Usage: 16.4 MB, less than 11.42% of Python online submissions for Minimum Window Substring.
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = collections.Counter(t)
        bucket = collections.defaultdict(int)
        j = 0
        ans = ""
        min_len = float('inf')
        form = 0

        # def is_valid():
        #     for k in counter:
        #         if bucket[k] < counter[k]:
        #             return False
        #     return True

        for i in range(len(s)):
            c = s[i]
            if c in counter:
                bucket[c] += 1
            if c in counter and bucket[c] == counter[c]:
                form += 1
            while form == len(counter):
                if i - j + 1 < min_len:
                    min_len = i - j + 1
                    ans = s[j:i + 1]
                if s[j] in counter:
                    bucket[s[j]] -= 1
                    if bucket[s[j]] < counter[s[j]]:
                        form -= 1
                j += 1

        return ans

print Solution().minWindow("ADOBECODEBANC","ABC")