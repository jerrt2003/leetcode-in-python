from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        self.s = s
        _, ans = self.dfs(0)
        return ans

    def dfs(self, idx: int) -> List:
        if idx == len(self.s):
            return [idx, ""]

        stack = []
        i = idx
        while i < len(self.s):
            if self.s[i] == "]":
                return [i, "".join(stack)]
            elif self.s[i] == "[":
                i, next_str = self.dfs(i + 1)
                stack.append(next_str)
            elif self.s[i].isdigit():
                if not stack:
                    stack.append(int(self.s[i]))
                elif stack[-1].isdigit():
                    prev_multiply = stack.pop()
                    multiply = 10 * prev_multiply + int(self.s[i])
                    stack.append(multiply)
                else:
                    tmp_str = ""
                    while not stack[-1].isdigit():
                        tmp_str = stack.pop() + tmp_str
                    multiply = stack.pop()
                    stack.append(multiply * tmp_str)
            elif self.s[i].isalpha():
                stack.append(self.s[i])
            i += 1

        return [i, "".join(stack)]
