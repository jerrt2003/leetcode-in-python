from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # 原地 Hashmap 
        # 要如何判斷一個數字有沒有出現過？最直覺方式就是使用hash(dict)
        # 但是題目要求space O(1), 所以不能用Hash
        # 但是題目說: all nums[i] are in the range of [1, n] 
        # 所以我們可以利用負號來判別數字是否出現過
        ret = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                ret.append(abs(num))
            else:
                nums[abs(num)-1] = -1 * nums[abs(num)-1]
        return ret
