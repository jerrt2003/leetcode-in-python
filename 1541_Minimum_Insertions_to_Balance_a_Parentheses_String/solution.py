import collections


class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        stack = collections.deque([])
        i = 0
        while i < len(s):
            # 假設遇到左括號，將其壓入棧
            if s[i] == "(":
                stack.append(s[i])
            # 假設遇到右括號，分下列情況：
            else:
                # 若棧為空 先補一個左括號
                if not stack:
                    stack.append("(")
                    ans += 1
                stack.pop()
                # 若下ㄧ個字元為右括號，則跳過(因為已經有兩個右括號可以匹配了)
                if i + 1 < len(s) and s[i + 1] == ")":
                    i = i + 1
                else:
                    # 否則補一個右括號
                    ans += 1
            i += 1

        # 最後若棧不為空，則每個左括號都要補兩個右括號
        ans += len(stack) * 2

        return ans
