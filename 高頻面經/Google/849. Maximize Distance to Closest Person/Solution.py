# -*- coding: utf-8 -*-
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        T: O(n)
        :type seats: List[int]
        :rtype: int
        """
        occupied = [i for i, v in enumerate(seats) if v == 1]
        maxDist = -float('inf')
        occupied.insert(0, 0)
        occupied.append(len(seats)-1)
        for i in range(len(occupied)-1):
            if occupied[i] == occupied[i+1]:
                continue
            else:
                if i == 0:
                    maxDist = max(maxDist, occupied[1])
                elif i == len(occupied)-2:
                    maxDist = max(maxDist, occupied[-1]-occupied[-2])
                else:
                    maxDist = max(maxDist, (occupied[i+1]-occupied[i])/2)
        return maxDist

assert Solution().maxDistToClosest([1,0,0,0,1,0,1]) == 2
assert Solution().maxDistToClosest([1,0,0,0]) == 3
