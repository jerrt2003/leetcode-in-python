import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # 分別統計 s, t 中各字母出現的次數
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)

        ans = 0
        for k, v in counter_t.items():
            # 假設 t 中有一個字母 k 並不在 s 中，則表示所有的 k 都要被替換
            # 即 ans += v
            if k not in counter_s.keys():
                ans += v
            else:
                # 若 k 在 t 中出現的次數比在 s 中出現的次數多，則在 t 中多出來的次數需要被替換
                diff = counter_t[k] - counter_s[k]
                if diff > 0:
                    ans += diff

        return ans
