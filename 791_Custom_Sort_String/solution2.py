import collections


# 模擬
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # 先統計 s 中每個字母出現的次數
        cnt = collections.defaultdict(int)
        for c in s:
            cnt[c] += 1
        ans = ""
        # 從 order 中的字母開始，如果在 cnt 中有出現，就把它加到 ans 中
        # 因為 order 本身有排序，所以會依照 order 的順序加入
        for c in order:
            if cnt[c] > 0:
                ans += c * cnt[c]
                del cnt[c]
        # 最後把剩下不在 order 的字母加到 ans 中
        for c, v in cnt.items():
            ans += c * v

        return ans
