# -*- coding: utf-8 -*-
class Solution(object):
    def multiply(self, num1, num2):
        """
        Perf: Runtime: 220 ms, faster than 33.65% / Memory Usage: 11.7 MB, less than 70.12%
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        res = [0]*(m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                p1 = i+j+1
                p2 = i+j
                sum = int(num1[i])*int(num2[j]) + res[p1]
                res[p1] = sum % 10
                res[p2] += sum / 10
        k = 0
        while k < len(res)-1:
            if res[k] == 0:
                k += 1
            else:
                break
        return ''.join([str(char) for char in res[k:]])

assert Solution().multiply('123','456') == '56088'