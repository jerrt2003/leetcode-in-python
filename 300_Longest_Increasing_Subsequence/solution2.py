# Patience Sorting
# 撲克牌遊戲

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            if not tails:
                tails.append(num)
                continue
            l, r = 0, len(tails)
            while l < r:
                m = (l + r - 1) // 2
                if tails[m] > num:
                    r = m
                else:
                    l = m + 1
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num
        return len(tails)
