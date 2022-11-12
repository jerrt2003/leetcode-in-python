# -*- coding: utf-8 -*-
class Solution:
    def nthUglyNumber(self, n):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/ugly-number-ii/discuss/69368/Elegant-C++-Solution-O(N)-space-time-with-detailed-explanation.
        Algorithm:
        - An ugly number is a number which prime number only consist of 2, 3, 5
        - As an ugly number, it must be fit either following condition:
            - x*2
            - y*3
            - z*5
            - x, y, z itself must be ugly number as well
            - !! thus we have a recurrence now..
        - But how to find x, y, z ??
        - Consider 1,2,3,4,5 what is the next ugly number?
            - x = 3 -> *2 = 6 > 5
            - y = 2 -> *3 = 6 > 5
            - z = 2 -> *5 = 10 > 5
            - since 6 < 10 thus 6 is next ugly number
            - increase x by 1
            - also need to increase y by 1 (now y=3) since 2*3=6 already being found
            - z remain the same
        - pseudo code:
        res = [1]
        i = 0, j=0, k=0
        for n in range(1, n):
            res.append(min(res[i]*2, res[j]*3, res[k]*5)
            if res[-1] == res[i]*2: i+=1
            if res[-1] == res[j]*3: j+=1
            if res[-1] == res[k]*5: k+=1
        return res[-1]
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        res = [1]
        i = 0
        j = 0
        k = 0
        for n in range(1, n): # we alrady have 1 in the list thus only need to loop n-1 times
            res.append(min(res[i]*2, res[j]*3, res[k]*5))
            if res[-1] == res[i]*2: i+=1
            if res[-1] == res[j]*3: j+=1
            if res[-1] == res[k]*5: k+=1
        return res[-1]

n = 10
sol = Solution()
print sol.nthUglyNumber(n)