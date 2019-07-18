# -*- coding: utf-8 -*-
class Solution(object):
    def printDiagonal(self, matrix):
        if not matrix:
            return None
        stack = [(0,0)]
        res = []
        while stack:
            _res = ''
            for _ in range(len(stack)):
                i, j = stack.pop(0)
                _res += matrix[i][j]
                for x, y in [(i, j+1), (i+1, j)]:
                    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and (x, y) not in stack:
                        stack.append((x, y))
            res.append(_res)
        return res

matrix = [
    ['a','b','c','d'],
    ['e','f','g','h'],
    ['i','m','n','q']
]

assert Solution().printDiagonal(matrix) == ['a','be','cfi','dgm','hn','q']