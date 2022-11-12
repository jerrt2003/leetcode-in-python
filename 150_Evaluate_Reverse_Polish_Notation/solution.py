class Solution(object):
    def evalRPN(self, tokens):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 60 ms, faster than 74.85% of Python online submissions for Evaluate Reverse Polish Notation.
        Memory Usage: 14.4 MB, less than 94.74% of Python online submissions for Evaluate Reverse Polish Notation.
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                p1 = stack.pop()
                p2 = stack.pop()
                sign = -1 if p1 * p2 < 0 else 1
                if t == '+':
                    _res = p2 + p1
                elif t == '-':
                    _res = p2 - p1
                elif t == '*':
                    _res = sign * (abs(p2) * abs(p1))
                else:
                    _res = sign * (abs(p2) / abs(p1))
                stack.append(_res)
            else:
                stack.append(int(t))
        return stack[-1]


print Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])