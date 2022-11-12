class Solution(object):
    def confusingNumberII(self, N):
        """
        Backtrack
        T:O(5^k) S:O(1)
        Runtime: 1244 ms, faster than 88.95% of Python online submissions for Confusing Number II.
        Memory Usage: 12.8 MB, less than 47.10% of Python online submissions for Confusing Number II.
        :type N: int
        :rtype: int
        """
        valid = [0, 1, 6, 8, 9]
        mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
        self.count = 0

        def dfs(v, rotation, digit):
            if v != rotation:
                self.count += 1
            for i in valid:
                if v*10+i > N:
                    break
                dfs(v*10+i, mapping[i]*digit*10+rotation, digit*10)

        dfs(1, 1, 1)
        dfs(6, 9, 1)
        dfs(8, 8, 1)
        dfs(9, 6, 1)

        return self.count


print Solution().confusingNumberII(20)
print Solution().confusingNumberII(100)