# -*- coding: utf-8 -*-
"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: list<list<Interval>>
        :rtype: list<Interval>
        """
        events = list()
        START, END = 1, 0
        for s in schedule:
            for _s in s:
                events.append((_s.start, START))
                events.append((_s.end, END))

        events.sort()
        ans = []
        bal = 0
        prev = None

        for evt in events:
            time = evt[0]
            action = evt[1]
            if bal == 0 and prev is not None:
                ans.append(Interval(prev, time))
            if action == START:
                bal += 1
            else:
                bal -= 1
            prev = time

        return ans