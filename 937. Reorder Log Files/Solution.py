# -*- coding: utf-8 -*-
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        Solution: Custom Sort
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        Perf: Runtime: 40 ms, faster than 19.84% / Memory Usage: 11.9 MB, less than 5.97%
        :type logs: List[str]
        :rtype: List[str]
        """
        l_logs = []
        d_logs = []
        for log in logs:
            if log.split(' ')[1].isdigit():
                d_logs.append(log)
            else:
                l_logs.append(log)
            l_logs.sort(key=self.getKey)
        return l_logs + d_logs


    def getKey(self, elem):
        first_space_idx = elem.find(' ')
        return elem[first_space_idx+1:], elem[:first_space_idx]
