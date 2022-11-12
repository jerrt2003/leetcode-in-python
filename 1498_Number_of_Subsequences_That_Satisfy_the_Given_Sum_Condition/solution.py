class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_q = []
        max_q = []
        ans = 0
        j = 0
        for num in nums:
            if not min_q or num >= min_q[-1]:
                min_q.append(num)
            else:
                while min_q and num < min_q[-1]:
                    min_q.pop()
                min_q.append(num)
            if not max_q or num <= max_q[-1]:
                max_q.append(num)
            else:
                while max_q and num > max_q[-1]:
                    max_q.pop()
                max_q.append(num)
            while min_q and max_q and min_q[0] + max_q[0] > target:
                if nums[j] == min_q[0]:
                    min_q.pop(0)
                if nums[j] == max_q[0]:
                    max_q.pop(0)
                j += 1
            ans += 1
        return ans


print Solution().numSubseq([3,5,6,7],9)
print Solution().numSubseq([3,3,6,8],10)