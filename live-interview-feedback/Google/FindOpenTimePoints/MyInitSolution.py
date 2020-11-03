# -*- coding: utf-8 -*-
class Solution(object):
    def findOpenSlot(self, intervals, query):
        intervals.sort(key=lambda x: x[0])
        merg_intervals = []
        for inte_s, inte_e in intervals:
            if not merg_intervals:
                merg_intervals.append([inte_s, inte_e])
            else:
                prev_s, prev_e = merg_intervals[-1][0], merg_intervals[-1][1]
                if inte_s >= prev_e:
                    merg_intervals.append([inte_s, inte_e])
                elif inte_e <= prev_e:
                    continue
                elif inte_s <= prev_s and inte_e >= prev_e:
                    merg_intervals[-1][1] = inte_e

        open_slots = []
        for i in range(len(merg_intervals)-1):
            open_s = merg_intervals[i][1]
            open_e = merg_intervals[i+1][0]
            open_slots.append([open_s, open_e])

        query_s, query_e = query[0], query[1]
        l, r = 0, len(open_slots)

        while l < r:
            m = (l+r-1)/2
            if open_slots[m] < query_s:
                l = m+1
            else:
                r = m

        total = 0
        for i in range(l, len(open_slots)):
            open_slots_s, open_slots_e = open_slots[i][0], open_slots[i][1]
            if query_e <= open_slots_s:
                break
            elif query_e <= open_slots_e:
                total += (query_e - open_slots_s)
            else:
                total += (open_slots_e - open_slots_s)

        return total

intervals = [[1,3],[2,4],[7,9],[11,13]]
query = [3,15]

print Solution().findOpenSlot(intervals, query)