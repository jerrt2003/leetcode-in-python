# -*- coding: utf-8 -*-
import math
class Solution(object):
    def isHappy(self, n):
        """
        Solution: Hash
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/happy-number/discuss/56913/Beat-90-Fast-Easy-Understand-Java-Solution-with-Brief-Explanation
        TP:
        - 如何判斷一個數是不是Happy Number..?
            - 假設這個數陷入一個無限循環,則我們可以知道這個數永遠不可能成為Happy Number
        - Create a dict
        - Use every sum we encounter as dict.
            - if we already see this "sum" in the dict, which means we are in a loop, thus return False
            - if sum == 1, return True
            - else continue to count
        :type n: int
        :rtype: bool
        """
        occured_sum = {}
        sum = n
        while sum != 1:
            tmp = 0
            while sum > 0:
                tmp += math.pow(sum%10,2)
                sum = sum/10
            tmp = int(tmp)
            if tmp == 1:
                return True
            elif occured_sum.has_key(tmp):
                return False
            else:
                occured_sum[tmp] = 1
            sum = tmp
        return True # take care of n = 1 situation
n = 19
sol = Solution()
print sol.isHappy(19)