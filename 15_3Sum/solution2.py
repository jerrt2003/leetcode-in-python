    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            ans = []
            for i in range(len(nums) - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        j += 1
                        continue
                    if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                        k -= 1
                        continue
                    num_sum = nums[i] + nums[j] + nums[k]
                    if num_sum == 0:
                        ans.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                    elif num_sum > 0:
                        k -= 1
                    else:
                        j += 1

            return ans
