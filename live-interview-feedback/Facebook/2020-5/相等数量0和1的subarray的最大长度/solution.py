class Solution(object):
    def longest(self, nums):
        """
        https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/
        T:O(n) S:O(n)
        Facebook
        :param arr:
        :return: int
        """
        nums = [-1 if num == 0 else num for num in nums]
        prefix, pre_sum = [], 0
        for num in nums:
            pre_sum += num
            prefix.append(pre_sum)
        table = dict()
        ans = -float('inf')
        for i, v in enumerate(prefix):
            if v == 0:
                ans = max(ans, i-0+1)
                continue
            if v not in table:
                table[v] = i
            else:
                ans = max(ans, i - table[v])
        return 0 if ans == -float('inf') else ans

# print Solution().longest([0,0,1,0,1,1,1,1,1,1])
# print Solution().longest([1,0,0,1,0,1,1])
# print Solution().longest([1,1,1,0,0])
print Solution().longest([1,1,1,1,1,1,1])