from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        stack = []
        for f in folder:
            if not stack or not (f.startswith(stack[-1]) and f[len(stack[-1])] == "/"):
                stack.append(f)

        return stack
