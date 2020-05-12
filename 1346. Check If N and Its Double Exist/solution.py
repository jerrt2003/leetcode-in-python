class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        visit = set()
        for num in arr:
            if num*2 in visit or (num % 2 == 0 and num/2 in visit):
                return True
            visit.add(num)
        return False

print Solution().checkIfExist([-2,0,10,-19,4,6,-8])