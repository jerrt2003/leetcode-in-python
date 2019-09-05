# -*- coding: utf-8 -*-
"""
有二十个骰子，每个骰子有六个面，每个面有一个字母或空字符串（用下划线代表），
输入一个phrase输出是否能用不同的骰子面（每个面只能用一次，可以用一个骰子的多个面）组合出这个phrase，返回值是<骰子#，面#>的vector

# 1. define data structure
d1: [(0,'a'),(1,'b'),(2,'c'),(3,'d'),(4,'e'),(5,'_')]

# 2. input: string
"""
import hash2
class Solution(object):
    def findCombo(self, dices, input):
        self.input = input
        self.charMap = hash2.defaultdict(list)
        for i, dice in enumerate(dices):
            for face, char in dice:
                self.charMap[char].append((i, face))
        self.res = None
        self._findPath([],[],0)
        return self.res

    def _findPath(self, res, visited, cur):
        if cur == len(self.input):
            self.res = res
            return
        target = self.input[cur]
        for dice, face in self.charMap[target]:
            if dice not in visited:
                self._findPath(res[:]+[(dice, face)], visited[:]+[dice], cur+1)


dices = [[(1,'a'),(2,'b'),(3,'c')],
         [(1,'d'),(2,'a'),(3,'f')],
         [(1,'h'),(2,'i'),(3,'b')]]

input = 'aab'

print Solution().findCombo(dices, input)