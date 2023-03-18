class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        l, r = 0, dividend+1
        while l < r:
            mid = (l+r-1)>>1
            if not self.quick_mul(divisor, mid, dividend):
                r = mid
            else:
                l = mid+1
        return l

    def quick_mul(self, x :int, y: int, target: int) -> bool:
        ans = 0
        while y > 0:
            if x & 1 == 1:
                ans += x
            x += x
            y = y >> 1
        if ans > target:
            return False
        return True