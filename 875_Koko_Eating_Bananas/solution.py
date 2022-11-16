from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)+1
        while l < r:
            m = (l+r-1)//2
            if self._finish(piles, m, h):
                r = m
            else:
                l = m+1
        return l
    
    def _finish(self, piles: List[int], speed: int, limit: int) -> bool:
        total_hr = 0
        for pile in piles:
            total_hr += pile//speed
            if pile%speed != 0:
                total_hr +=1
            if total_hr > limit:
                return False
        return total_hr <= limit