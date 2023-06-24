class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1)-1, len(num2)-1
        ans = []
        carry = 0
        while m >= 0 or n >= 0:
            d1 = self.convert(num1[m]) if m >= 0 else 0
            d2 = self.convert(num2[n]) if n >= 0 else 0
            ans.append((d1+d2+carry) % 10)
            carry = (d1+d2+carry) // 10
            if m >= 0:
                m -= 1
            if n >= 0:
                n -= 1
        if carry != 0:
            ans.append(1)
        
        return ''.join(str(num) for num in ans[::-1])
    
    def convert(self, num: str) -> int:
        return ord(num) - ord('0')