# -*- coding: utf-8 -*-
class Solution(object):
    def findAllCombo(self):
        str = '123456789'
        self.res = []

        def dfs(str, curr_sum, path):
            if curr_sum == 100 and len(str) == 0:
                self.res.append(path)
                return
            elif len(str) == 0:
                return
            for i in range(len(str)):
                num = int(str[:i+1])
                next_str = str[i+1:]
                dfs(next_str, curr_sum+int(num), path[:]+[num])
                dfs(next_str, curr_sum-int(num), path[:]+[-num])
            return

        dfs(str, 0, [])
        print self.res
        for nums in self.res:
            sum = 0
            for num in nums:
                sum += num
            print sum

Solution().findAllCombo()