import collections
from typing import List


class Solution:
    def findRLEArray(
        self, encoded1: List[List[int]], encoded2: List[List[int]]
    ) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(encoded1) and j < len(encoded2):
            count = 0
            while encoded1[i][1] > 0 and encoded2[j][1] > 0:
                count += 1
                encoded1[i][1] -= 1
                encoded2[j][1] -= 1
            if not ans or ans[-1][0] != encoded1[i][0] * encoded2[j][0]:
                ans.append([encoded1[i][0] * encoded2[j][0], count])
            else:
                ans[-1][1] += count
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1

        return ans
