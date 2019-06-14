import collections


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeMap = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.timeMap[key].append((value, timestamp))
        #self.timeMap[key].sort(key=lambda x: x[1]) <-- don't need the sort since timestamp

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.timeMap.keys():
            return ""
        else:
            lst = self.timeMap[key]
            l, r = 0, len(lst) - 1
            while l <= r:
                m = (l + r) / 2
                if lst[m][1] == timestamp:
                    return lst[m][0]
                elif lst[m][1] > timestamp:
                    r = m - 1
                else:
                    l = m + 1
            return lst[l-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)