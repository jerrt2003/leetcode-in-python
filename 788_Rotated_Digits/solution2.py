class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        d = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1] + [0] * (n - 9)
        for i in range(n + 1):
            if d[i // 10] == -1 or d[i % 10] == -1:
                d[i] = -1
            elif d[i // 10] == 1 or d[i % 10] == 1:
                d[i] = 1
                ans += 1

        return ans
