class Solution:
    def mySqrt(self, x: int) -> int:
        l: int = 0
        r: int = x+1
        if x == 0: return 0
        while l < r:
            m = (l+r-1)//2
            if m*m - x > 0:
                r = m
            else:
                l = m+1
        return l-1