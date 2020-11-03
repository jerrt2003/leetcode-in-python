class Solution(object):
    def findMaxConcurrentWorker(self, workers):
        """
        T:O(nlog(n)) S:O(1)
        :param workers: List[List]
        :return: int
        """
        workers.sort(key=lambda x: x[1])
        ans = 0
        concurr_worker = 0
        prev_s, prev_e = 0, 0
        for _, s, e in workers:
            if s > prev_e:
                ans = max(ans, concurr_worker)
                concurr_worker = 1
                prev_s, prev_e = s, e
            else:
                concurr_worker += 1
                prev_s, prev_e = max(prev_s, s), min(prev_e, e)
        return ans

print Solution().findMaxConcurrentWorker([[1,2,8],[2,5,6],[3,14,15],[4,12,17],[5,3,9]])