# -*- coding: utf-8 -*-
class SnapShot(object):
    """
    Time Complexity:
    - Get: O(nlog(v))
    - Put: O(1)
    - Snapshot: O(1)
    Space Complexity: O(nv) --> store only changes between version

    """
    def __init__(self, arr):
        self.arr = [[[0, v]] for v in arr] # [ver, val]
        self.ver = 0

    def put(self, idx, val):
        # to store changing history
        curr = self.arr[idx][-1]
        curr_ver = curr[0]
        if curr_ver == self.ver:
            curr[1] = val
        else:
            self.arr[idx].append([self.ver, val])

    def get(self, ver=None):
        if ver > self.ver:
            return None
        res = []
        if ver is None:
            for _change_history in self.arr:
                _last_change = _change_history[-1]
                res.append(_last_change[1])
        else:
            for _change_history in self.arr:
                idx = self.bs(_change_history, ver)
                _change = _change_history[idx]
                res.append(_change[1])
        return res

    def bs(self, lst, ver):
        l, r = 0, len(lst)
        while l < r:
            m = (l+r-1)/2
            if lst[m][0] == ver:
                return m
            elif lst[m][0] > ver:
                r = m
            else:
                l = m+1
        return l-1

    def snap(self):
        self.ver += 1
        return self.ver - 1


s = SnapShot([0, 0])
s.snap() # ver 0 [0,0]
s.put(0, 1)
s.snap() # ver 1 [1,0]
s.put(1,3)
s.put(0,2)
s.snap() # ver 2 [2,3]
print s.get()
