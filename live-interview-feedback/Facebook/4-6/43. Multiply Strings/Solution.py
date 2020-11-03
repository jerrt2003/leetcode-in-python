# -*- coding: utf-8 -*-
class Solution(object):
    def multiply(self, num1, num2):
        """
        Solution: Using digit multiply
        Time Complexity: O(n^2)
        Space Complexity: O(m+n)
        Inspired By: https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
        TP:
        - 針對每一位數字作傳統的乘法運算
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len_num1 = len(num1)
        len_num2 = len(num2)
        res = [0] * (len_num1+len_num2)
        for i in range(len_num1-1, -1, -1):
            for j in range(len_num2-1, -1, -1):
                curr = int(num1[i])*int(num2[j])
                p1 = i+j
                p2 = i+j+1
                sum = curr + res[p2]
                res[p1] = res[p1] + sum/10
                res[p2] = sum%10
        res = ''.join([str(i) for i in res])
        zero_position = 0
        while zero_position < len(res)-1 and res[zero_position] == '0':
            zero_position += 1
        return res[zero_position:]

num1 = '123'
num2 = '456'

sol = Solution()
print sol.multiply(num1,num2)
