class SnapshotArray(object):

    def __init__(self, length):
        """
        Runtime: 588 ms, faster than 32.91% of Python online submissions for Snapshot Array.
        Memory Usage: 51.1 MB, less than 100.00% of Python online submissions for Snapshot Array.
        S:O(n)
        :type length: int
        """
        self.history = [[[0,0]] for _ in range(length)] #[ver, value]
        self.ver = 0

    def set(self, index, val):
        """
        T:O(1)
        :type index: int
        :type val: int
        :rtype: None
        """
        last = self.history[index][-1] # last = [ver, value]
        if last[0] == self.ver:
            last[1] = val
        else:
            self.history[index].append([self.ver, val])

    def snap(self):
        """
        T:O(1)
        :rtype: int
        """
        self.ver += 1
        return self.ver-1


    def get(self, index, snap_id):
        """
        T:(log(n))
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        if snap_id > self.ver:
            return None
        return self.bs(self.history[index], snap_id)


    def bs(self, lst, snap_id):
        l, r = 0, len(lst)
        while l < r:
            mid = (l+r-1)/2
            if lst[mid][0] > snap_id:
                r = mid
            else:
                l = mid+1
        return lst[l-1][1]




# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)