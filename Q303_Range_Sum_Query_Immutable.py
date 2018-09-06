class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        ------- TOP BOTTOM SOLUTION -----
        self.nums = nums
        self.sum = dict()
        ---------------------------------
        """
        # DP: Bottom-Up Solution
        if nums is None or len(nums) == 0:
            return 0
        self.nums = nums
        self.sum = dict()
        if not isinstance(nums[0],int):
            self.sum = None
            return
        self.sum[0] = nums[0]
        for i in range(1, len(nums)):
            if not isinstance(nums[i],int):
                self.sums = None
                return
            self.sum[i] = self.sum[i-1] + self.nums[i]


    def sumRange(self, i, j):
        """
        DP: TOP to Bottom Solution
        :type i: int
        :type j: int
        :rtype: int
        if i == j:
            result = self.nums[i]
            self.sum[(i, j)] = result
            return result
        if (i, j) in self.sum.keys():
            return sum[(i, j)]
        else:
            result = self.sumRange(i, j-1) + self.nums[j]
            self.sum[(i, j)] = result
            return result
        """
        # DP: Bottom-Up Solution
        if self.sum is None:
            return None
        return self.sum[j] - self.sum[i] + self.nums[i]


#nums = [-2, 0, 3, -5, 2, -1]
nums = [[]]
sol = NumArray(nums)
print sol.sumRange(4,5)
