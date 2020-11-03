# -*- coding: utf-8 -*-
class Solution(object):
    def cokeMachine(self, buttons, targetLow, targetHigh):
        self.DP = dict()
        self.low = targetLow
        self.high = targetHigh
        self.buttons = buttons
        return self.dfs(0, 0)

    def dfs(self, low, high):
        if (low, high) in self.DP:
            return self.DP[(low, high)]
        if self.low <= low and high <= self.high:
            return True
        if high > self.high:
            return False
        for l, h in self.buttons:
            if self.dfs(low+l, high+h):
                self.DP[(low, high)] = True
                return True
        self.DP[(low, high)] = False
        return False


buttons = [[100, 120], [200, 240], [400, 410]]
target_low, target_high = 100, 110
assert Solution().cokeMachine(buttons, target_low, target_high) == False

buttons = [100, 120], [200, 240], [400, 410]
target_low, target_high = 100, 110
assert Solution().cokeMachine(buttons, target_low, target_high) == False
target_low, target_high = 90, 120
assert Solution().cokeMachine(buttons, target_low, target_high) == True
target_low, target_high = 300, 360
assert Solution().cokeMachine(buttons, target_low, target_high) == True
target_low, target_high = 310, 360
assert Solution().cokeMachine(buttons, target_low, target_high) == False
target_low, target_high = 1, 999999
assert Solution().cokeMachine(buttons, target_low, target_high) == True


