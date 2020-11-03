class Solution(object):
    def findKthSmallest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(l, r):
            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def quickSelect(l, r, k):
            pos = partition(l, r)
            if pos == k-1:
                return pos
            elif pos < k:
                return quickSelect(pos+1, r, k)
            else:
                return quickSelect(l, pos-1, k)

        x = quickSelect(0, len(nums)-1, k)
        return nums[x]


print Solution().findKthSmallest([1,2,3,4,5,6,7], 2)