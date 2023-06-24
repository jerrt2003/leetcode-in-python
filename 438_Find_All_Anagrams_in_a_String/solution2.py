from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_counter = [0] * 26
        curr_counter = [0] * 26
        ans = []
        l, r = 0, 0

        # get p's counter
        for char in p:
            target_counter[ord(char) - ord("a")] += 1

        while r < len(s):
            curr_counter[ord(s[r]) - ord("a")] += 1
            if r - l + 1 == len(p):
                if curr_counter == target_counter:
                    ans.append(l)
                curr_counter[ord(s[l]) - ord("a")] -= 1
                l += 1
            r += 1

        return ans
