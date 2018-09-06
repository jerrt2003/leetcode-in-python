class Solution(object):
    '''
    def canPartitionKSubsets(self, nums, k):
        """
        For each bucket, try all possible values
        Time Complexity: O(k*2^n)
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = 0
        for num in nums:
            total += num
        if total % k != 0:
            return False
        target = total / k

        def search(groups):
            if not nums:
                return True # all value being used
            value = nums.pop()
            for i in range(len(groups)):
                if groups[i] + value <= target:
                    groups[i] += value
                    if search(groups):
                        return True
                    groups[i] -= value # deduct the value from groups[i] if not matched
            nums.append(value)
            return False

        nums.sort()
        if nums[-1] > target:
            return False # if any number > target then no way we can return True
        while nums and nums[-1] == target:
            k -= 1
            nums.pop() # pop num which equal to target
        return search([0]*k)
    '''

    def canPartitionKSubsets(self, nums, k):
        """
        For each nums, try all possible buckets
        Time Complexity: O(n^k)
        :param nums:
        :param k:
        :return:
        """
        # find bucket size
        total = 0
        for num in nums:
            total += num
        if total % k != 0: return False
        target = total / k
        nums.sort(reverse=True)

        def search(buckets):
            all_bucket_is_full = True
            for bucket in buckets:
                if bucket != target:
                    all_bucket_is_full = False
                    break
                else:
                    continue
            if all_bucket_is_full:
                return True
            for idx in range(len(nums)):
                value = nums.pop(idx)
                for i in range(len(buckets)):
                    if buckets[i] + value <= target:
                        buckets[i] += value
                        if search(buckets):
                            return True
                        buckets[i] -= value
                nums.insert(idx, value)
                return False

        for num in nums:
            if num > target: return False
            elif num == target:
                nums = nums[1:]
                k -= 1
        if k == 0:
            return True

        return search([0]*k)

test = {'nums':[4, 3, 2, 3, 5, 2, 1], 'k':4}
#nums = [4, 3, 2, 3, 5, 2, 1]
#nums = [7628,3147,7137,2578,7742,2746,4264,7704,9532,9679,8963,3223,2133,7792,5911,3979]
#test = {'nums':[3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269], 'k':5}
sol = Solution()
print sol.canPartitionKSubsets(test['nums'], test['k'])