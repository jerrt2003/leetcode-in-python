# -*- coding: utf-8 -*-
class Soltuion(object):

    def printSoltion(self, input):

        res = ['']

        def findCombo(i, string):
            cache = ''
            while i < len(string) and string[i] != '}':
                cache += string[i]
                i += 1
            return cache.split(','), i

        idx = 0
        while idx < len(input):
            if input[idx] == '{':
                combo, idx = findCombo(idx+1, input)
                res = [a + b for a in res for b in combo]
            else:
                res = [a + input[idx] for a in res]
            idx += 1

        print ','.join(res)


Soltuion().printSoltion('a{{f, g},c}d')