from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans :List[List[int]] = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                return ans
            if i > 0 and num == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                num_sum = num + nums[j] + nums[k]
                if num_sum == 0:
                    while j < k and nums[j] == nums[j+1]: # !! 須在num_sum==0之後不然會有答案被忽略
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1                    
                    ans.append([num, nums[j], nums[k]])
                    k -= 1
                    j += 1
                elif num_sum > 0:
                    k -= 1
                else:
                    j += 1
        return ans
