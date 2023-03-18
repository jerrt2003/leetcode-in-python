class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            # 若為左括號 無論如何先入棧
            if c == "(":
                stack.append(i)
            elif c == ")":
                # 若為右括號 當棧為空或是棧最上層元素非左括號 則此括號為無效 => 入棧
                if not stack or s[stack[-1]] != "(":
                    stack.append(i)
                else:
                    # 若棧最上層為左括號 則當前括號可與最上層括號配對 => 左括號出棧
                    stack.pop()
        ans = ""
        stack = set(stack)
        for i, c in enumerate(s):
            if i not in stack:
                ans += c
        return ans