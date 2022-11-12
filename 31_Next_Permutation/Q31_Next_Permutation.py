class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start_idx = len(nums) - 1
        while start_idx > 0:
            if nums[start_idx -1] >= nums[start_idx]:
                start_idx -= 1
                continue
            else:
                p = len(nums) - 1
                while p > start_idx -1:
                    if nums[p] > nums[start_idx -1]:
                        tmp = nums[p]
                        nums[p] = nums[start_idx -1]
                        nums[start_idx -1] = tmp
                        break
                    else:
                        p -= 1
                nums[start_idx:len(nums)] = nums[start_idx:len(nums)][::-1] # reverse the substring
                print nums
                return
        nums.sort()
        print nums

#a = [1,2,7,4,3,1]
a = [5,1,1]
sol = Solution()
sol.nextPermutation(a)