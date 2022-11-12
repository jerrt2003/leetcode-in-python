class Solution(object):
    # def findKthLargest(self, nums, k):
    #     """
    #     T:O(n) S:O(1)
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     l, r = 0, len(nums)-1
    #     pos = self.quickSelect(nums, l, r, k)
    #     return nums[pos]
    #
    # def quickSelect(self, nums, l, r, k):
    #     pos = self.partition(nums, l, r)
    #     if pos == k-1:
    #         return pos
    #     elif pos < k:
    #         return self.quickSelect(nums, pos+1, r, k)
    #     else:
    #         return self.quickSelect(nums, l, pos-1, k)
    #
    # def partition(self, nums, l, r):
    #     pivot = nums[r]
    #     i = l
    #     for j in range(l, r):
    #         if nums[j] > pivot:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             i += 1
    #     nums[i], nums[r] = nums[r], nums[i]
    #     return i
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.nums = nums
        pos = self.quickSelect(0, len(nums) - 1, k)
        return self.nums[pos]

    def quickSelect(self, l, r, k):
        pos = self.partition(l, r)
        if pos == k - 1:
            return pos
        if pos < k:
            return self.quickSelect(pos+1, r, k)
        else:
            return self.quickSelect(l, pos-1, k)

    def partition(self, l, r):
        pivot = self.nums[r]
        i = l

        for j in range(l, r):
            if self.nums[j] > pivot:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                i += 1

        self.nums[r], self.nums[i] = self.nums[i], self.nums[r]
        return i


print Solution().findKthLargest([3,2,1,5,6,4], 2)