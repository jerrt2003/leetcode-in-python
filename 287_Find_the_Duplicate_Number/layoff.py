from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # 如何將node.next 對應到本題？
        # 142 题中慢指针走一步 slow = slow.next ==> 本题 slow = nums[slow]
        # 142 题中快指针走两步 fast = fast.next.next ==> 本题 fast = nums[nums[fast]]
        while nums[slow] and nums[fast] and nums[nums[fast]]:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                tmp = 0
                while tmp != slow:
                    tmp = nums[tmp]
                    slow = nums[slow]
                return slow