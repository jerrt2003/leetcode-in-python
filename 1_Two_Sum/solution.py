from typing import Dict, List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_map: Dict[int, int] = {}
        for idx, num in enumerate(nums):
            if target - num in num_idx_map.keys():
                return [num_idx_map[target-num], idx]
            else:
                num_idx_map[num] = idx
        return [0, 0]