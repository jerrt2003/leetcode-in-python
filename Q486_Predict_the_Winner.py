class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.score_a = 0
        self.score_b = 0
        self._predictTheWinner(nums, turn='a')
        if self.score_a < self.score_b:
            return False
        else:
            return True

    def _predictTheWinner(self, nums, turn=None):
        if len(nums) == 0:
            return
        elif turn == 'a':
            tmp_a = self._predictTheWinner(nums[1:], turn='b')
            tmp_b = self._predictTheWinner(nums[:-1], turn='b')
            


score = [1, 5, 2]
sol = Solution()
print sol.PredictTheWinner(score)