class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            # 升冪單調棧
            # 什麼數字會越小？越小的數字越前面越小
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # 當k還沒用完時 由於stack會是個升冪單調棧 所以排除後面位數
        while k > 0:
            stack.pop()
            k -= 1
        
        while stack and stack[0] == '0':
            stack.pop(0)

        return '0' if not stack else "".join(stack)