# -*- coding: utf-8 -*-
class Solution(object):
    def printAllCombo(self, inputs):
        def _printAllCombo(inputs, res):
            if not inputs:
                return res
            input = inputs.pop(0)
            res = [a+b for a in res for b in input]
            return _printAllCombo(inputs, res)

        res = _printAllCombo(inputs, [''])
        print res

Solution().printAllCombo([['US','JP','EU'],['1','2','3'],['@','#','$']])