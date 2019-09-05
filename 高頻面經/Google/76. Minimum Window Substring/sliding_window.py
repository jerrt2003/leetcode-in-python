# -*- coding: utf-8 -*-
from hash2 import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        Solution: Sliding Window
        Time Complexity: O(s+t)
        Space Complexity: O(s+t)
        Inspired By: https://leetcode.com/problems/minimum-window-substring/solution/
        TP:
        - using sliding window
            - use 2 pointer l, r to mark the start-end of the window
            - Once we found the window includes all the char(s) required, we'll do:
                - continue to contracting the window (l+=1) till the window is no longer include all required char(s)
            - then we move r by 1 (r+=1) and repeat above steps till we visit whole s
        - Key point:
            - Collection: Counter class
            - tuple to store answer
        :type s: str
        :type t: str
        :rtype: str
        """
        required_char = Counter(t)
        required_distinct_char = len(required_char)
        l, r = 0, 0
        res = float('inf'), l, r
        formed = 0
        current_window_char = dict()
        while r < len(s):
            char_r = s[r]
            current_window_char[char_r] = current_window_char.get(char_r, 0)+1
            if char_r in required_char and current_window_char[char_r] == required_char[char_r]:
                formed += 1
            while l <= r and formed == required_distinct_char:
                char_l = s[l]
                if r - l + 1 < res[0]:
                    res = r - l + 1, l, r
                l += 1
                current_window_char[char_l] -= 1
                if current_window_char[char_l] < required_char[char_l]:
                    formed -= 1
            r += 1
        return "" if res[0] == float('inf') else s[res[1]:res[2]+1]

S = "A"
T = "AA"
print Solution().minWindow(S,T)