class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        Facebook
        Stack
        T:O(n) S:O(n)
        Runtime: 1732 ms, faster than 17.60% of Python online submissions for Minimum Remove to Make Valid Parentheses.
        Memory Usage: 18.3 MB, less than 27.38% of Python online submissions for Minimum Remove to Make Valid Parentheses.
        :type s: str
        :rtype: str
        """
        # stack = []
        # for i, c in enumerate(s):
        #     if c == "(" or c == ")":
        #         if not stack or c == "(":
        #             stack.append(i)
        #         elif c == ")" and s[stack[-1]] == "(":
        #             stack.pop()
        #         else:
        #             stack.append(i)
        # stack = set(stack)
        # ans = ""
        # for i in range(len(s)):
        #     if i not in stack:
        #         ans += s[i]
        # return ans
        """
        Stack
        T:O(n) S:O(1)
        Runtime: 120 ms, faster than 94.88% of Python online submissions for Minimum Remove to Make Valid Parentheses.
        Memory Usage: 18.9 MB, less than 12.02% of Python online submissions for Minimum Remove to Make Valid Parentheses.
        """
        s = [c for c in s]
        count = 0
        for i, c in enumerate(s):
            if c == "(":
                count += 1
            elif c == ")":
                if count == 0:
                    s[i] = ""
                else:
                    count -= 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(" and count > 0:
                s[i] = ""
                count -= 1
            if count == 0:
                break
        return ''.join(s)

# print Solution().minRemoveToMakeValid("lee(t(c)o)de)")
print Solution().minRemoveToMakeValid("())()(((")