class Solution(object):
    def videoStitching(self, clips, T):
        """
        Greedy
        T:O(nlog(n)) S:O(1)
        Runtime: 16 ms, faster than 94.89% of Python online submissions for Video Stitching.
        Memory Usage: 12.8 MB, less than 20.00% of Python online submissions for Video Stitching.
        Solution: https://www.youtube.com/watch?v=tEx3z4L7F-c
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        cur_end = -1
        potential_end = 0
        ans = 0
        for i, j in sorted(clips):
            if i > potential_end or potential_end >= T:
                break
            if cur_end < i <= potential_end:
                ans += 1
                cur_end = potential_end
            potential_end = max(potential_end, j)
        return ans if potential_end >= T else -1


print Solution().videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10)