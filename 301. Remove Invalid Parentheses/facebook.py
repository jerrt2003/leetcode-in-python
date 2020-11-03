class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        Facebook
        DFS
        Stack
        Backtrack
        Runtime: 56 ms, faster than 82.86% of Python online submissions for Remove Invalid Parentheses.
        Memory Usage: 12.7 MB, less than 83.89% of Python online submissions for Remove Invalid Parentheses.
        :type s: str
        :rtype: List[str]
        """

        def get_remove_count(s):
            l = r = 0
            for c in s:
                if c == '(':
                    l += 1
                elif c == ')' and l > 0:
                    l -= 1
                elif c == ')':
                    r += 1
            return l, r

        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        def dfs(s, start, l, r):
            if l == 0 and r == 0 and isValid(s):
                ans.append(''.join(s))
                return
            for i in range(start, len(s)):
                if i != start and s[i] == s[i - 1]:
                    continue
                if s[i] == ')' and r > 0:
                    dfs(s[:i] + s[i + 1:], i, l, r - 1)
                if s[i] == '(' and l > 0:
                    dfs(s[:i] + s[i + 1:], i, l - 1, r)

        ans = []
        l, r = get_remove_count(s)
        dfs(s, 0, l, r)
        return ans

print Solution().removeInvalidParentheses("()())()")