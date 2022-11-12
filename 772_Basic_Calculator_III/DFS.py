# -*- coding: utf-8 -*-
class Solution(object):
    def calculate(self, s):
        """
        T: O(n)
        S: O(n)
        Perf: Runtime: 40 ms, faster than 84.44% / Memory Usage: 12.1 MB, less than 100.00%
        :type s: str
        :rtype: int
        """
        s = s + '$'
        def dfs(i):
            stack = []
            num = 0
            sign = '+'
            while i < len(s):
                c = s[i]
                if c == ' ':
                    i += 1
                    continue
                if c.isdigit():
                    num = num*10 + int(c)
                    i += 1
                elif c == '(':
                    num, i = dfs(i+1)
                    i += 1
                else:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-1 * num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        if stack[-1] < 0:
                            stack.append(-1 * (abs(stack.pop())/num))
                        else:
                            stack.append(stack.pop()/num)
                    if s[i] == ')':
                        return sum(stack), i
                    i += 1
                    num = 0
                    sign = c
            return sum(stack), i

        return dfs(0)[0]

#assert Solution().calculate("1 + 1") == 2
#assert Solution().calculate(" 6-4 / 2 ") == 4
#assert Solution().calculate("2*(5+5*2)/3+(6/2+8)") == 21
assert Solution().calculate("(2+6* 3+5- (3*14/7+2)*5)+3") == -12
assert Solution().calculate("5 - 3/2") == 4