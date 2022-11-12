class Solution(object):
    def nextGreaterElements(self, nums):
        """
        Facebook
        Stack + Mono-Q
        T:O(n) S:O(n)
        Runtime: 220 ms, faster than 65.62% of Python online submissions for Next Greater Element II.
        Memory Usage: 14.6 MB, less than 45.28% of Python online submissions for Next Greater Element II.
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [-1] * len(nums)
        stack = []
        for i in range(2 * len(nums)):
            idx = i % len(nums)
            while stack and nums[idx] > nums[stack[-1]]:
                ans[stack.pop()] = nums[idx]
            stack.append(idx)

        return ans

print Solution().nextGreaterElements([1,2,1])


