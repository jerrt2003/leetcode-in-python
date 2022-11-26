from typing import Dict, List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        self.prefix_sum_count: Dict[int, int] = defaultdict(int)
        self.prefix_sum_count[0] = 1
        self.prefix_sums: List[int] = []
        
        for num in nums:
            if len(self.prefix_sums) == 0:
                self.prefix_sums.append(num)
                self.prefix_sum_count[num] += 1
            else:
                prev_sum = self.prefix_sums[-1]
                self.prefix_sum_count[prev_sum+num] += 1
                self.prefix_sums.append(prev_sum+num)
        
        ans: int = 0
        for prefix_sum in self.prefix_sums:
            key = prefix_sum - k
            if key in self.prefix_sum_count.keys():
                ans += self.prefix_sum_count[key]

        return ans