class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.arr = arr
        

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        _arr = self.arr[left:right+1]
        maj, count = _arr[0], 1
        for i in range(1, len(_arr)):
            if maj == _arr[i]:
                count += 1
            elif count == 0:
                maj = _arr[i]
                count += 1
            else:
                count -= 1
        
        freq = 0
        for num in _arr:
            if num == maj:
                freq += 1

        return maj if freq >= threshold else -1

sol = MajorityChecker([1,1,2,2,1,1])
sol.query(0,5,4)        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)