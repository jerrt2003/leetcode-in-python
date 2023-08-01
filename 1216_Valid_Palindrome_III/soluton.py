# Based on #680
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if k == 0:
                    return False
                return self.isValidPalindrome(s[l:r], k - 1) or self.isValidPalindrome(
                    s[l + 1 : r + 1], k - 1
                )
        return True
