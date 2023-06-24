import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # hashmap to record char's freq of target
        t_counter = collections.Counter(t)
        # hashmap to record current window char counter
        s_counter = collections.defaultdict(int)
        # counter to record if current substring meet requirement
        form = 0
        # l, r is boudary
        l, r = 0, 0

        # var to record final ans
        ans = ""
        min_len = float("inf")

        while r < len(s):
            if s[r] in t_counter.keys():
                s_counter[s[r]] += 1
                if s_counter[s[r]] == t_counter[s[r]]:
                    form += 1
            while form == len(t_counter):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = s[l : r + 1]
                if s[l] in t_counter.keys():
                    s_counter[s[l]] -= 1
                    if s_counter[s[l]] < t_counter[s[l]]:
                        form -= 1
                l += 1
            r += 1

        return ans
