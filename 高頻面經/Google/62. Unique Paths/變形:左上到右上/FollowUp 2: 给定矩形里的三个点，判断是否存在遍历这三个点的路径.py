# -*- coding: utf-8 -*-
class Solution(object):
    def canReach(self, cords):
        cords.sort(lambda cord: cord[0])
        for idx in range(1, len(cords)):
            prev_i, prev_j =  cords[idx-1][0], cords[idx-1][1]
            curr_i, curr_j = cords[idx][0], cords[idx][1]
            if prev_i == curr_i:
                return False
            radius = curr_j - prev_j
            lower = prev_i - radius
            upper = prev_i + radius
            if lower <= curr_i <= upper:
                continue
            else:
                return False
        return True