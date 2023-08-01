class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = []
        while n > 0:
            nums.append(n % 10)
            n = n // 10
        nums = nums[::-1]

        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        if i >= 0:
            while k > i and nums[i] >= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]
            l, r = j, len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            ans = 0
            multi = 1
            for i in range(len(nums) - 1, -1, -1):
                ans += multi * nums[i]
                multi *= 10
            if ans > 2**31 - 1:
                return -1
            return ans
        else:
            return -1
