class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        self.nums = nums
        return self.dfs(0, len(nums) - 1)

    def dfs(self, s: int, e: int) -> int:
        if s == e:
            return s
        m = (s + e) // 2
        if self.nums[m] > self.nums[m + 1]:
            return self.dfs(s, m)
        else:
            return self.dfs(m + 1, e)
