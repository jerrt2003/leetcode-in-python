# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l, r = 0, 10001
        while l < r:
            m = (l+r-1)//2
            ret = reader.get(m)
            if ret > target or ret == 2^31-1:
                r = m
            else:
                l = m+1
        if l == 0 or reader.get(l-1) != target:
            return -1
        return l-1
        