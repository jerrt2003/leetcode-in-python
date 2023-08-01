from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            si, ei = firstList[i][0], firstList[i][1]
            sj, ej = secondList[j][0], secondList[j][1]
            if si <= sj <= ei or sj <= si <= ej:
                ans.append([max(si, sj), min(ei, ej)])
            if ei <= ej:
                i += 1
            else:
                j += 1
        return ans
