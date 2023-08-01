import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        sCounter = collections.Counter(s)
        maxLen = max(sCounter.values())
        # 先判斷是否有可能有解
        # 當字串長度為奇數時，同一字母最多出現 (len(s) + 1) / 2 次
        # 當字串長度為偶數時，同一字母最多出現 len(s) / 2 次
        if (len(s) % 2 == 1 and maxLen > (len(s) + 1) / 2) or (
            len(s) % 2 == 0 and maxLen > len(s) / 2
        ):
            return ""

        # 從出現頻率最高的字母開始排
        sCounter = sorted(sCounter.items(), key=lambda x: -x[1])
        ans = ["" for _ in range(len(s))]
        idx = 0

        for k, v in sCounter:
            while v > 0:
                ans[idx] = k
                v -= 1
                idx += 2
                # 一旦 idx 超過字串長度，就從 1 開始排 (i.e. 偶數位排完了回頭排奇數位)
                if idx >= len(s):
                    idx = 1

        return "".join(ans)
