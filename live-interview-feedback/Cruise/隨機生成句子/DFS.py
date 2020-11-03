# -*- coding: utf-8 -*-
import random
class Solution(object):
    def generate(self, startKey, maps):
        self.maps = maps
        self.res = []
        self.dfs(self.maps[startKey])
        return ' '.join(self.res)

    def dfs(self, input):
        m = len(input)
        idx = random.randint(0, m-1)
        if type(input[idx]) == list:
            for w in input[idx]:
                if w[0].isupper():
                    self.dfs(self.maps[w])
                else:
                    self.res.append(w)
        else:
            self.res.append(input[idx])




maps = {'S': [['NP','VP'],['S','and','S']],
        'NP' : [['Art', 'N']],
        'VP' : [['V', 'NP']],
        'Art' : ['the', 'a'],
        'N' : ['man', 'ball', 'woman', 'table'],
        'V' : ['hit', 'took', 'saw', 'liked']
        }
print Solution().generate('S', maps)