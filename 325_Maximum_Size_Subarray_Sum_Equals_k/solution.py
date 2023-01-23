from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # 本題與2-sum思路類似 只是多加了prefix-sum的概念
        ans = -float('inf')
        n = len(nums)
        # 利用哈希表紀錄曾經出現的前綴和
        val_to_idx = {0: 0}
        prefix_sum = [0] * (n+1)
        for i in range(1, n+1):
            # prefix_sum[i]: 在nums[i-1](包含)處的前綴和
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
            # prefix_sum[i] - prefix_sum[x] == k 
            # -> prefix_sum[i] - prefix_sum[x] == y
            # prefix_sum[x]為某前綴和
            # 假設prefix_sum[x]已經在之前出現過 則表示我們有個長度為i-x的子串符合條件
            # !為什麼是i-x -> 因為prefix_sum[x]為包含x的前綴和 所以長度應為i-x而非i-x+1
            if prefix_sum[i]-k in val_to_idx.keys():
                ans = max(ans, i - val_to_idx[prefix_sum[i]-k])
            if prefix_sum[i] not in val_to_idx.keys():
                val_to_idx[prefix_sum[i]] = i
        return 0 if ans == -float('inf') else ans
