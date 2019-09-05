# -*- coding: utf-8 -*-
from hash2 import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        Sol: Using OrderedDict
        Perf: Speed 42.89% / Usage 74.11%
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.cache = LastUpdatOrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.cache[key] = self.cache[key]
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key] = value
            return
        if self.count == self.capacity:
            self.cache.popitem(last=False)
            self.count -= 1
        self.cache[key] = value
        self.count += 1

class LastUpdatOrderedDict(OrderedDict):
    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)