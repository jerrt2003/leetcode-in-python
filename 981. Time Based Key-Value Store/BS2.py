# -*- coding: utf-8 -*-
import collections


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = collections.defaultdict(list)
        self.value = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        T:O(1), S:O(n)
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.time[key].append(timestamp)
        self.value[key].append(value)

    def get(self, key, timestamp):
        """
        T:(log(n))
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        lst = self.time[key]
        l, r = 0, len(lst)
        while l < r:
            mid = (l + r - 1) / 2
            if lst[mid] > timestamp:
                r = mid
            else:
                l = mid + 1
        return '' if l == 0 else self.value[key][l - 1]


time = TimeMap()
time.set('love','high',10)
time.set('love','low',20)
time.get('love',5)