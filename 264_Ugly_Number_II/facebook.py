class Solution(object):
    def nthUglyNumber(self, n):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 120 ms, faster than 82.47% of Python online submissions for Ugly Number II.
        Memory Usage: 12.7 MB, less than 84.09% of Python online submissions for Ugly Number II.
        :type n: int
        :rtype: int
        """
        ans = [1]
        i2 = i3 = i5 = 0
        for _ in range(n-1):
            min_n = min(ans[i2]*2, ans[i3]*3, ans[i5]*5)
            if min_n == ans[i2]*2:
                i2 += 1
            if min_n == ans[i3]*3:
                i3 += 1
            if min_n == ans[i5]*5:
                i5 += 1
            ans.append(min_n)
        return ans[-1]

print Solution().nthUglyNumber(10)