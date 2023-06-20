class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for k, v in enumerate(s):
            if v == "(":
                stack.append(k)
            else:
                stack.pop()
                if stack:
                    ans = max(ans, k-stack[-1])
                else:
                    stack.append(k)
        return ans


