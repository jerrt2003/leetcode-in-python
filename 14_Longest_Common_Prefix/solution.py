from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = strs[0]
        for word in strs[1:]:
            idx = 0
            while idx < min(len(ans), len(word)):
                if ans[idx] != word[idx]:
                    break
                idx += 1
            ans = ans[:idx]
            if len(ans) == 0:
                break
        return ans