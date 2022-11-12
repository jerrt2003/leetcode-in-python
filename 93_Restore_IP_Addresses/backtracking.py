# -*- coding: utf-8 -*-
import re
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        Solution: Backtracking
        Time Complexity:
        Space Complexity:
        Inspired by: MYSELF!!
        TP:
        - A ip address has total of 3 '.'(dots)
        - So we go through the list and decrease 'dot' count in each recursion
            - when count == 1 means we reached the last section of the IP, we can
                - add result if the IP so far is valid
                - or just return when IP is not valid
        - We can break the for loop when current section is already not valid
        - Improvement: use regex
        :type s: str
        :rtype: List[str]
        """
        self.pattern = re.compile('(^[1-2]?[0-5]?[0-5]?$|^0$)')
        self.res = []
        try:
            int(s)
        except:
            return self.res
        for i in range(1,len(s)):
#            if (int(s[:i]) <= 255 and not s[:i].startswith('0')) or (int(s[:i]) == 0 and len(s[:i]) == 1):
            if self.pattern.match(s[:i]):
                self.findIP(s[i:], 3, s[:i]+".")
            else:
                break
        return self.res

    def findIP(self, s, count, current_ip):
        if count == 1:
#            if (int(s) <= 255 and not s.startswith('0')) or (int(s) == 0 and len(s) == 1):
            if self.pattern.match(s):
                self.res.append(current_ip+s)
                return
            else:
                return
        for i in range(1, len(s)):
#            if (int(s[:i]) <= 255 and not s[:i].startswith('0')) or (int(s[:i]) == 0 and len(s[:i]) == 1):
            if self.pattern.match(s[:i]):
                self.findIP(s[i:], count-1, current_ip+s[:i]+'.')
            else:
                break

s = "010010"
#s = '25525511135'
#s = '0'
sol = Solution()
print sol.restoreIpAddresses(s)