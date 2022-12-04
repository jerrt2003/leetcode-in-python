from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        path = []
        self.helper(0, len(nums), path, sorted(nums))
        return self.ret

    def helper(self, start: int, end: int, path: List[int], nums: List[int]) -> None:
        if start > end:
            return                   
        self.ret.append(path) 
        for i in range(start, end):
            self.helper(i+1, end, path+[nums[i]], nums)