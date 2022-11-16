from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        min_div, max_div = 1, max(nums)
        while min_div < max_div:
            m = (min_div + max_div)//2
            if not self._exceed_threshold(nums, m, threshold):
                max_div = m
            else:
                min_div = m+1
        return min_div

    def _exceed_threshold(self, nums: List[int], div: int, threshold: int) -> bool:
        total_sum = 0
        for num in nums:
            total_sum += num // div
            if num % div !=0:
                total_sum += 1
            if total_sum > threshold:
                return True
        return total_sum > threshold
