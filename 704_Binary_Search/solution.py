from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l+r-1)//2
            if nums[m] > target:
                r = m
            else:
                l = m+1
        # return l-1 if nums[l-1] == target else -1
        if nums[l-1] == target:
            return l-1
        else:
            return -1

if __name__ == "__main__":
    s = Solution()
    # print(s.search([-1,0,3,5,9,12], 2))
    print(s.search([5], -5))
                