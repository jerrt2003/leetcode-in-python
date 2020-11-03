import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        Facebook
        Sliding Window + Monoq
        T:O(n) S:O(n)
        Runtime: 300 ms, faster than 80.39% of Python online submissions for Sliding Window Maximum.
        Memory Usage: 23.2 MB, less than 61.84% of Python online submissions for Sliding Window Maximum.
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        monoq = collections.deque([])
        ans = []
        j = 0
        for num in nums:
            k -= 1
            if not monoq or num < monoq[-1]:
                monoq.append(num)
            else:
                while monoq and num > monoq[-1]:
                    monoq.pop()
                monoq.append(num)
            if k == 0:
                ans.append(monoq[0])
                if nums[j] == monoq[0]:
                    monoq.popleft()
                j += 1
                k += 1
        return ans

# print Solution().maxSlidingWindow([1,3,-1,-3,5,4,6,7], 3)
# print Solution().maxSlidingWindow([1,-1], 1)
print Solution().maxSlidingWindow([1,3,1,2,0,5],3)