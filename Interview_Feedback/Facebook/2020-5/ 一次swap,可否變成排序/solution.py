class Solution(object):
    def checkIfSwap(self, nums):
        sort_nums = sorted(nums)
        count = 0
        for n1, n2 in zip(nums, sort_nums):
            if n1 != n2:
                count += 1
            if count > 2:
                return False
        return True


print Solution().checkIfSwap([1,4,3,2,5])
print Solution().checkIfSwap([5,4,3,2,1])