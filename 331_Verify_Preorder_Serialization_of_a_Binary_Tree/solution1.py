from typing import Any, List

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # solution 1: stack method
        stack: List[str] = []
        preorder = preorder.split(",")
        while preorder:
            node = preorder.pop(0)
            stack.append(node)
            # 为了兼容这两个情况，我们想出了本题的一个重磅级的技巧：把有效的叶子节点使用 "#" 代替。 比如把 4## 替换成 # 。此时，叶子节点会变成空节点！
            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#" and stack[-3] != "#":
                stack.pop(), stack.pop(), stack.pop()
                stack.append("#")
        return len(stack) == 1 and stack[0] == "#"