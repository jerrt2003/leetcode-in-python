class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(l, r):
            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def quickSelect(l, r, k):
            p = partition(l, r)
            if p == k-1:
                return nums[p]
            elif p < k:
                return quickSelect(p+1, r, k)
            else:
                return quickSelect(l, p-1, k)

        return quickSelect(0, len(nums) - 1, k)


print Solution().findKthLargest([3,2,1,5,6,4],2)