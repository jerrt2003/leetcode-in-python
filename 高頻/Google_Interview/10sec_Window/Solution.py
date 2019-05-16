# -*- coding: utf-8 -*-
from datetime import datetime
class Solution(object):
    def printDataNotIn10SecWindow(self, inputs):
        ts_log = dict()
        for input in inputs:
            data, ts = input.split('@')
            if data not in ts_log:
                print input
                ts_log[data] = datetime.strptime(ts, '%H:%M:%S')
            else:
                prev_ts = ts_log[data]
                curr_ts = datetime.strptime(ts, '%H:%M:%S')
                diff = (curr_ts - prev_ts).total_seconds()
                if diff > 10:
                    print input
                    ts_log[data] = datetime.strptime(ts, '%H:%M:%S')

inputs = ["a@01:00:00", "b@01:00:02", "c@00:00:06","a@01:00:08", "a@01:00:11"]

Solution().printDataNotIn10SecWindow(inputs)