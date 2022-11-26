import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_w: List[int] = []
        for _w in w:
            if len(self.prefix_w) == 0:
                self.prefix_w.append(_w)
            else:
                prev_w_sum = self.prefix_w[-1]
                self.prefix_w.append(prev_w_sum+_w)

    def pickIndex(self) -> int:
        weight = random.randint(1, self.prefix_w[-1]) #單位為1的數軸
        l, r = 0, len(self.prefix_w)
        while l < r:
            m = (l+r-1)//2
            if self.prefix_w[m] >= weight:
                r = m
            else:
                l = m+1
        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()