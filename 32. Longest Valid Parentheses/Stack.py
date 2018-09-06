# -*- coding: utf-8 -*-
class Solution(object):
    def longestValidParentheses(self, s):
        """
        Solution: Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/longest-valid-parentheses/solution/
        Note:
        1. Create a stack
        2. Pushing -1 into stack
        3. Scanning the 's' and do following:
        - if s[i] is '(', push its idx into stack
        - if s[i] is ')', pop the stack (because we only push idx into stack if s[idx] is '(' so its ok to pop it) and
        we subtract current idx to top-most of stack to get maximum len
        - if stack becomes empty, push current idx into stack
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        if len_s == 0: return 0
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] is '(':
                stack.append(i)
            else:
                stack.pop() # 因為我們只會在s[i] is '(' 的情況下將idx append到stack,所以可以作pop()
                if len(stack) == 0: # 表示重新計算max_len
                    stack.append(i)
                else:
                    max_len = max(max_len, i-stack[-1])
        return max_len

input = "(()"
sol = Solution()
print sol.longestValidParentheses(input)


