# -*- coding: utf-8 -*-
class Solution(object):
    def canJump(self, nums):
        """
        Solution: DP / Top-Bottom (left->right + Memorization)
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        TP:
        - Use DP to memorize each index result so we won't need to revisit that idx again
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return True
        last_idx = len(nums) - 1

        DP = set()

        def DFS(idx):
            if nums[idx] == 0 or idx in DP:
                return False
            for jump in range(1, nums[idx]+1):
                next = jump + idx
                if next == last_idx:
                    return True
                elif next > last_idx:
                    break
                else:
                    if DFS(next):
                        return True
                    DP.add(next)
            return False
        return DFS(0)

nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print Solution().canJump(nums)
