import collections


class Solution:
    def checkValidString(self, s: str) -> bool:
        # 建立两个栈，一个存左括号的位置，一个存星号的位置
        stack_left_p = collections.deque([])
        stack_star = collections.deque([])

        for i, c in enumerate(s):
            # 若遇到左括号，将其位置压入栈
            if c == "(":
                stack_left_p.append(i)
            # 若遇到右括号，分下列情况：
            elif c == ")":
                # 若左括号栈不为空，则弹出栈顶元素(找到匹配的左括号)
                if stack_left_p:
                    stack_left_p.pop()
                # 若左括号栈为空且星号栈不为空，则弹出栈顶元素(将星号作为左括号)
                elif stack_star:
                    stack_star.pop()
                # 若左括号栈为空且星号栈为空，则返回False (沒有左括号或是星號可以匹配)
                else:
                    return False
            else:
                stack_star.append(i)

        # 若最後左括号栈不为空
        while stack_left_p:
            # 若星号栈为空，则返回False(沒有星號可以匹配)
            if not stack_star:
                return False
            left_p_pos = stack_left_p.pop()
            star_pos = stack_star.pop()
            # 若星號的下標不大於左括号的下標，则返回False(星號在左括号的左邊)
            if left_p_pos > star_pos:
                return False

        return True
