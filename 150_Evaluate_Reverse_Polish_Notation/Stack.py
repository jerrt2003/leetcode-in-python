# -*- coding: utf-8 -*-
class Solution(object):
    def evalRPN(self, tokens):
        """
        Solution: Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://en.wikipedia.org/wiki/Reverse_Polish_notation
        TP:
        (from Wiki sudo code)
            for each token in the postfix expression:
            if token is an operator:
                operand_2 ← pop from the stack
                operand_1 ← pop from the stack
                result ← evaluate token with operand_1 and operand_2
                push result back onto the stack
            else if token is an operand:
                push token onto the stack
                result ← pop from the stack
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operends = set(['+','-','*','/'])
        for token in tokens:
            if token in operends:
                p1 = stack.pop()
                p2 = stack.pop()
                if token == '+': p = p2+p1
                elif token == '-': p = p2-p1
                elif token == '*': p = p2*p1
                else:
                    if p2*p1 < 0: # !! 6/-132 = -1
                        p = -1 * (abs(p2)/abs(p1))
                    else:
                        p = p2/p1
                stack.append(p)
            else:
                stack.append(int(token))
        return stack[-1]

tokens =  ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print Solution().evalRPN(tokens)