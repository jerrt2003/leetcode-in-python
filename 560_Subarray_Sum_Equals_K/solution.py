import collections

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counter = collections.defaultdict(int)
        # by default 前綴和為0的數組為1(因爲啥都沒有)
        prefix_counter[0] = 1
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            key = prefix_sum - k
            if key in prefix_counter.keys():
                ans += prefix_counter[key]
            prefix_counter[prefix_sum] += 1
        return ans