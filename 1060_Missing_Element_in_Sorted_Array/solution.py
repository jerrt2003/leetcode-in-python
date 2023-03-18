from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # miss_count_list是一個差距的list
        # 例如[4,7,9,10]，miss_count_list就是[0,2,3,3] -> 代表4和7之間有2個數字，7和9之間有3個數字，9和10之間有3個數字
        # 這樣的話，我們就可以知道，如果k=3，那麼就是在7和9之間，因為4和9之間有3個miss數字，所以k=3就是8
        miss_count_list: List[int] = [0]
        miss_count = 0
        for i in range(0, len(nums)-1):
            diff = nums[i+1] - nums[i] - 1
            miss_count += diff
            miss_count_list.append(miss_count)
        
        l, r = 0, len(nums)
        while l < r:
            mid = (l+r-1)//2
            if miss_count_list[mid] >= k:
                r = mid
            else:
                l = mid+1
        # 在這邊我們不需要考慮l=0的情況，因為如果l=0，而miss_count_list[0] = 0
        # 代表k本身會是小於0的數字，不會有這種情況發生
        return nums[l-1] + (k - miss_count_list[l-1])