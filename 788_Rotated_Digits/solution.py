class Solution:
    def rotatedDigits(self, n: int) -> int:
        digit_status = [-1 for _ in range(n + 1)]
        ans = 0
        divisor = 1
        for num in range(n + 1):
            if num < 10:
                if num in [2, 5, 6, 9]:
                    digit_status[num] = 1
                    ans += 1
                elif num in [0, 1, 8]:
                    digit_status[num] = 0
                else:
                    digit_status[num] = -1
            else:
                if num / divisor >= 10:
                    divisor *= 10
                r = num % divisor
                q = num // divisor
                if q in [2, 5, 6, 9] and digit_status[r] != -1:
                    digit_status[num] = 1
                    ans += 1
                elif q in [0, 1, 8] and digit_status[r] == 1:
                    digit_status[num] = 1
                    ans += 1
                elif q in [0, 1, 8] and digit_status[r] == 0:
                    digit_status[num] = 0

        return ans
