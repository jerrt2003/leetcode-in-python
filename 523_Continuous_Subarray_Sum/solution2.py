from typing import List, Dict

class Solution:
    # 這題的解法是用餘數來做
    # 假如有兩個數 a, b，且 a % k = b % k -> a - b % k = 0 -> a - b = n * k
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # rem_2_idx是一個字典，key是餘數，value是index
        # 這個字典的目的是為了找到兩個餘數相同的index
        # hash起始為{0:-1}的目的是為了處理類似[23,2,4,6,6], k=7這種情況
        # [23,2,4,6]符合條件 -> sum([23,2,4,6]) = 35 -> 35 % 7 = 0
        rem_2_idx: Dict[int, int] = {0: -1}
        rem = 0
        for i, v in enumerate(nums):
            rem += v
            rem %= k
            if rem in rem_2_idx.keys() and i - rem_2_idx[rem] >= 2:
                return True
            rem_2_idx[rem] = i
        return False