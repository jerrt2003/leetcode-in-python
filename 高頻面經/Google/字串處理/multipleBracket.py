# -*- coding: utf-8 -*-
class Solution(object):

    def dfs(self, s):
        finalResult = ''
        result = ['']
        inBrace = False
        currentWord = ''
        currentQueue = []
        for i in s:
            if i is '{':
                inBrace = True
            elif i is '}':
                inBrace = False
                currentQueue.append(currentWord)
                currentWord = ''
                result = [a + b for b in currentQueue for a in result]
                currentQueue = []
            elif i is ',' and inBrace:
                currentQueue.append(currentWord)
                currentWord = ''
            elif i is ',':
                result = [a + i for a in result]
                finalResult = finalResult + ','.join(result)
                result = ['']
            else:
                if not inBrace:
                    result = [a + i for a in result]
                else:
                    currentWord += i
        return finalResult + ','.join(result)


input = 'a{{1,2},b}c'

print Solution().dfs(input)
