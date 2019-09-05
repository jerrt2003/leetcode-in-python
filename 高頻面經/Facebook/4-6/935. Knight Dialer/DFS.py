# -*- coding: utf-8 -*-
import hash2,math
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 10
        self.nextJump = {1:(6,8),2:(7,9),3:(4,8),4:(0,3,9),5:(),6:(0,1,7),7:(2,6),8:(1,3),9:(2,4),0:(4,6)}
        self.uniquePath = hash2.defaultdict(int)
        self.mod = math.pow(10,9)+7
        count = 0
        for dial in xrange(10):
            count += self.dfs(dial, N-1)
        return count % (10 ** 9 + 7)

    def findSymetric(self, dial):
        if dial == 1: return 3
        if dial == 2: return 8
        if dial == 3: return 1
        if dial == 4: return 6
        if dial == 6: return 4
        if dial == 7: return 9
        if dial == 8: return 2
        if dial == 9: return 7
        return dial

    def dfs(self, dial, N):
        if (dial, N) in self.uniquePath:
            return self.uniquePath[(dial, N)]
        elif (self.findSymetric(dial), N) in self.uniquePath:
            return self.uniquePath[(self.findSymetric(dial), N)]
        if N == 0:
            return 1
        _count = 0
        for nextDial in self.nextJump[dial]:
            self.uniquePath[(nextDial, N-1)] = self.dfs(nextDial, N-1)
            _count += self.uniquePath[(nextDial, N-1)]
        return _count

#assert Solution().knightDialer(1) == 10
#assert Solution().knightDialer(2) == 20
assert Solution().knightDialer(3) == 46
#assert Solution().knightDialer(100) == 46