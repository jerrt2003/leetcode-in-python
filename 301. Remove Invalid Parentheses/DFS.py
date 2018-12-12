# -*- coding: utf-8 -*-
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        Solution: DFS
        Time Complexity: O(2^(l+r))
        Space Complexity: O(n^(l+r))
        Inspired By: https://www.youtube.com/watch?v=2k_rS_u6EBk
        TP:
        - THIS IS GOD DAMN HARD !!!
        - First we scan the string to determine min left '(' or right ')' need to be removed from original string
            - def findRemoveParentheseCount(self, s)
            - using stack to count
            - if char == '(', left += 1
            - elif char == ')' and left > 0 -> means there is an open '(' -> left -= 1
            - elif char == ')', right += 1
            - at the end either left > 0 or right > 0 since '(' and ')' should be a pair and it will be 相互抵銷掉
        - Now we know how many '(' or ')' need to be removed then we can start doing DFS
            - !!! 注意事項:
                - If we hit consecutive '(' or ')', we only removed the first one to eliminate duplicate
                - As recursive goes, we decrease l (or r) by 1 and start with the last-deleted index
                - When l == 0 and r == 0, which means no more '(' or ')' need to be deleted, then we can check if final answer is valid
                    - def isValid(self, s)
                    - if yes then we append it to our final answer self.res
        :type s: str
        :rtype: List[str]
        """
        self.findRemoveParentheseCount(s)
        self.res = []
        self.dfs([char for char in s], 0, self.l, self.r)
        return self.res

    def dfs(self, curr, start, l, r):
        if l == 0 and r == 0: # no more '(' or ')' need to be removed
            if self.isValid(curr):
                self.res.append(''.join(curr))
            return
        for i in range(start, len(curr)):
            # WHY i != start ??
            # 1. In any given scenarios we only delete multiple '('s or ')'s <- referred to above TP
            # 2. If we found i == start and curr[i] need to be deleted (curr[i] == '(' or ')') it means the previous
            # character must be just deleted (since if i == start means we just got inside this recursion) thus we
            # don't need to delete this one
            #
            # SO WHY the 2nd condition: curr[i] == curr[i-1]
            # Ans: 當我們從前一個delete的遞迴出來後下一個萬一若是同一個符號(ex. '((' or '))' ) 則我們不需要delete第二個(因為上一個
            # 已經處理過了
            if i != start and curr[i] == curr[i-1]:
                continue
            if curr[i] == '(' or curr[i] == ')':
                if r > 0 and curr[i] == ')':
                    new_curr = curr[:]
                    new_curr.pop(i)
                    self.dfs(new_curr, i, l, r-1)
                elif l > 0 and curr[i] == '(':
                    new_curr = curr[:]
                    new_curr.pop(i)
                    self.dfs(new_curr, i, l-1, r)

    def findRemoveParentheseCount(self, s):
        """
        To find how many "(" and ")" need to be removed to make the s valid
        :param s:
        :return: None
        """
        self.l = self.r = 0
        for char in s:
            if char == '(':
                self.l += 1
            elif char == ')' and self.l > 0:
                self.l -= 1
            elif char == ')':
                self.r += 1

    def isValid(self, s):
        stack = 0
        for char in s:
            if char == '(':
                stack += 1
            if char == ')':
                stack -= 1
            if stack < 0:
                return False
        return stack == 0

input = "()())()"
sol = Solution()
print sol.removeInvalidParentheses(input)