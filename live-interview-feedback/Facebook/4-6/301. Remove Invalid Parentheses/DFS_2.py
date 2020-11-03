# -*- coding: utf-8 -*-
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            total = 0
            for _s in s:
                if _s == '(':
                    total += 1
                elif _s == ')':
                    total -= 1
                    if total < 0:
                        return False
            return total == 0

        def parenthesesToBeDeleted(s):
            """
            Check how many '(' and ')' need to be removed respectively
            :param s:
            :return:
            """
            l, r = 0, 0
            for _s in s:
                if _s == '(':
                    l += 1
                elif _s == ')':
                    if l == 0:
                        r += 1
                    else:
                        l -= 1
            return l, r

        def dfs(s, start, l, r, ans):
            if l == 0 and r == 0:
                if isValid(s):
                    ans.append(''.join(s))
                return
            for i in range(start, len(s)):
                if i != start and s[i] == s[i-1]:
                    continue
                if s[i] in ('(', ')'):
                    next_s = s[:i] + s[i+1:]
                    if r > 0 and s[i] == ')':
                        dfs(next_s, i, l, r-1, ans)
                    elif l > 0 and s[i] == '(':
                        dfs(next_s, i, l-1, r, ans)

        res = []
        s = list(s)
        l, r = parenthesesToBeDeleted(s)
        dfs(s, 0, l, r, res)

        return res

Solution().removeInvalidParentheses("()())()")