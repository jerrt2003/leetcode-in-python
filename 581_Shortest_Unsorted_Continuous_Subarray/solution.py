from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = float("inf"), -float("inf")
        mono_stack = []
        for i in range(len(nums)):
            while mono_stack and nums[i] < nums[mono_stack[-1]]:
                start = min(start, mono_stack.pop())
            mono_stack.append(i)

        mono_stack = []
        for i in range(len(nums) - 1, -1, -1):
            while mono_stack and nums[i] > nums[mono_stack[-1]]:
                end = max(end, mono_stack.pop())
            mono_stack.append(i)

        return max(end - start + 1, 0)
