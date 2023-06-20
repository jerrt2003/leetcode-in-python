class Solution:
    def isPalindrome(self, x: int) -> bool:
        return self.math(x)

    def convert_method(self, x: int) -> bool:
        s = str(x)[::-1]
        return str(x) == s
    
    def math(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10
        while x > 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div = div // 100
        return True