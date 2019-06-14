# -*- coding: utf-8 -*-
class Solution(object):
    def validString(self, str):
        curMax = ord('A')
        for i in range(len(str)):
            if i == 0 and ord(str[i]) != ord('A'):
                return False
            elif ord(str[i]) > curMax+1:
                return False
            curMax = max(ord(str[i]), curMax)
        return True

#assert Solution().validString('AAAABAC') == True
assert Solution().validString('BCD') == False
assert Solution().validString('ABCAABC') == True
assert Solution().validString('ABCAABCF') == False
assert Solution().validString('ABCAABCD') == True
