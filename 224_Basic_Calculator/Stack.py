# -*- coding: utf-8 -*-
class Solution(object):
    def calculate(self, s):
        """
        Facebook
        Runtime: 92 ms, faster than 94.97% of Python online submissions for Basic Calculator.
        Memory Usage: 14.8 MB, less than 42.29% of Python online submissions for Basic Calculator.
        Solution: Interactive Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/basic-calculator/discuss/62361/Iterative-Java-solution-with-stack
        TP:
        - Only 5 possible input we need to pay attention:
            - digit: it should be one digit from the current number
            - '+': number is over, we can add the previous number and start a new number
            - '-': same as above
            - '(': push the previous result and the sign into the stack, set result to 0, just calculate the new result within the parenthesis.
            - ')': pop out the top two numbers from stack, first one is the sign before this pair of parenthesis, second is the temporary result before this pair of parenthesis. We add them together.
        - Finally if there is only one number, from the above solution, we haven't add the number to the result, so we do a check see if the number is zero
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        curr_num = 0
        sign = 1
        for elem in s:
            if elem.isdigit():
                curr_num = 10*curr_num + int(elem)
            elif elem == '+':
                res += curr_num * sign
                curr_num = 0
                sign = 1
            elif elem == '-':
                res += curr_num * sign
                curr_num = 0
                sign = -1
            elif elem == '(':
                stack.append(res)
                stack.append(sign)
                #curr_num = 0 // no need, must be reset to 0 before
                res = 0
                sign = 1
            elif elem == ')':
                res += curr_num * sign
                res *= stack.pop()
                res += stack.pop()
                # sign = 1 // no need, since if following is a '+' or '-', it will hit res += curr_sum * sign while curr_sum is 0 already thus '+' or '-' doesn't take any effect
                curr_num = 0
        if curr_num != 0:
            res += sign * curr_num
        return res

# s = "2147483647"
s = '(1+(4+5+2)-3)+(6+8)'
print Solution().calculate(s)