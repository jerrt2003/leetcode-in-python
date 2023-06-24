import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counters = collections.Counter(s)
        seen = set()
        stack = []
        for c in s:
            if c not in seen:
                while stack and c < stack[-1] and counters[stack[-1]] > 0:
                    char = stack.pop()
                    seen.remove(char)
                stack.append(c)
                seen.add(c)
            counters[c] -= 1

        return "".join(stack)
