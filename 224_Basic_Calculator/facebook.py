class Solution(object):
    def calculate(self, s):
        """
        Facebook
        divide and conquer
        T:O(n) S:O(n)
        Runtime: 108 ms, faster than 85.62% of Python online submissions for Basic Calculator.
        Memory Usage: 14.7 MB, less than 49.05% of Python online submissions for Basic Calculator.
        each bracket stands for a level "result"
        (1+(2+3)+4)-(1+2)
        ----------R  ---- R
           ----R
        :type s: str
        :rtype: int
        """
        curr = 0
        res = 0
        stack = []
        sign = 1
        for _s in s:
            if _s.isdigit():
                curr = 10 * curr + int(_s)
            elif _s in ['+', '-']:
                res += sign * curr
                curr = 0
                sign = 1 if _s == '+' else -1
            elif _s == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif _s == ')':
                res += sign * curr
                res *= stack.pop()
                res += stack.pop()
                curr = 0
        if curr != 0:
            res += curr * sign

        return res

# print Solution().calculate("(1+(4+5+2)-3)+(6+8)")
print Solution().calculate("1-(5)")