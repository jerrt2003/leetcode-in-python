# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        l, r = 0, col
        while l < r:
            mid = (l+r-1) // 2
            if self.check_row(row, mid, binaryMatrix):
                r = mid
            else:
                l = mid+1
        return l if l != col else -1

    def check_row(self, row: int, col: int, binaryMatrix: 'BinaryMatrix') -> bool:
        for i in range(0, row):
            if binaryMatrix.get(i, col) == 1:
                return True
        return False
            
