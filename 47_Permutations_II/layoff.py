from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ret: List[int] = []
        self.helper(sorted(nums), [])
        return self.ret
    
    def helper(self, nums: List[int], path: List[int]) -> None:
        if not nums:
            self.ret.append(path)
            return
        for i, v in enumerate(nums):
            # 剪枝 
            # 假設數組為 [1,1,2] 當遍歷以第一個數1為開頭時剩下的數組為[1,2] 
            # 而當遍歷以第二個數字1為開頭時剩下的數組也是[1,2]
            # 所以可以剪枝(i.e.第一個數組已經遍歷過了)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.helper(nums[:i]+nums[i+1:], path + [nums[i]])
        