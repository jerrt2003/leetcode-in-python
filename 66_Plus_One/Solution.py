# -*- coding: utf-8 -*-
class Solution(object):
    def plusOne(self, digits):
        """
        Solution: array
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MYSELF!!
        TP:
        - Traverse backward (using step (-1))
        - Consider carry(進位)
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = True
        for i in range(len(digits)-1,-1,-1):
            if carry:
                digits[i] += 1
                if digits[i] == 10:
                    digits[i] = 0
                else:
                    carry = False
        if carry:
            digits.insert(0,1)
        return digits

digits = [1,2,3]
sol = Solution()
print sol.plusOne(digits)