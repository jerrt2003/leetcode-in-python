# Sorting
import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        charCounter = collections.Counter(s)
        ans = ""
        for k in sorted(
            [k for k in charCounter.keys()], key=lambda x: charCounter[x], reverse=True
        ):
            ans += k * charCounter[k]

        return ans
