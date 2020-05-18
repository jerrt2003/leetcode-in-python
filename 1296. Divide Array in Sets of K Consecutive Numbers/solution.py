import collections


class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        T:O(nlogn+nk) S:O(n)
        Runtime: 444 ms, faster than 66.17% of Python online submissions for Divide Array in Sets of K Consecutive Numbers.
        Memory Usage: 28.4 MB, less than 100.00% of Python online submissions for Divide Array in Sets of K Consecutive Numbers.
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # nums.sort()
        # if len(nums) % k != 0: return False
        #
        # counter = collections.Counter(nums)
        # total = len(nums)
        # for num in nums:
        #     if total == 0:
        #         break
        #     if counter[num] == 0:
        #         continue
        #     else:
        #         counter[num] -= 1
        #         for i in range(num+1, num+k):
        #             if counter[i] == 0:
        #                 return False
        #             else:
        #                 counter[i] -= 1
        #         total -= k
        # return True
        if len(nums) % k != 0: return False
        counter = collections.Counter(nums)
        for i in sorted(counter.keys()):
            cnt = counter[i]
            if cnt > 0:
                for next_i in range(i+1, i+k):
                    if counter[next_i] < cnt:
                        return False
                    else:
                        counter[next_i] -= cnt
        return True





# print Solution().isPossibleDivide([1,2,3,3,4,4,5,6], 4)
# print Solution().isPossibleDivide([1,2,3,3,3,4,5,6], 4)
# print Solution().isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], 3)
print Solution().isPossibleDivide([3,3,2,2,1,1],3)