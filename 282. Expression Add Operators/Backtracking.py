# -*- coding: utf-8 -*-
class Solution(object):
    def addOperators(self, num, target):
        """
        Solution: DFS(backtracking)
        T: O(n*n)
        S: O(n*n)
        Perf: Runtime: 1576 ms, faster than 15.69% / Memory Usage: 12.2 MB, less than 50.00%
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.res = []
        self.target = target
        for i in range(1, len(num)+1):
            currNum = num[:i]
            if i == 1 or (i > 1 and currNum[0] != '0'):
                self.dfs(int(currNum), currNum, num[i:], int(currNum))
        return self.res


    def dfs(self, currSum, path, rem, lastNum):
        if currSum == self.target and len(rem) == 0:
            self.res.append(path)
        for i in range(1, len(rem)+1):
            currNum = rem[:i]
            if i == 1 or (i > 1 and currNum[0] != '0'):
                self.dfs(currSum + int(currNum), path+'+'+currNum, rem[i:], int(currNum))
                self.dfs(currSum - int(currNum), path+'-'+currNum, rem[i:], -int(currNum))
                self.dfs(currSum - lastNum + lastNum*int(currNum), path+'*'+currNum, rem[i:], lastNum*int(currNum))

num = "123"
target = 6
#assert Solution().addOperators(num, target) == ["1+2+3", "1*2*3"]

num = "105"
target = 5
assert Solution().addOperators(num, target) == ["1*0+5","10-5"]
