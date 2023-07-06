from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1 for _ in range(n)]
        stack = []
        for i in range(2 * n):
            idx = i % n
            if not stack:
                stack.append(idx)
            else:
                while stack and nums[idx] > nums[stack[-1]]:
                    ans[stack.pop()] = nums[idx]
                stack.append(idx)

        return ans
