class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 72 ms, faster than 76.52% of Python online submissions for Exclusive Time of Functions.
        Memory Usage: 12.8 MB, less than 60.00% of Python online submissions for Exclusive Time of Functions.
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        stack = []
        for log in logs:
            tmp = log.split(":")
            job_id, job_type, ts = tmp[0], tmp[1], tmp[2]
            job_id = int(job_id)
            ts = int(ts)
            if job_type == "start":
                stack.append([job_id, ts, 0])
            else:
                _, start_ts, delay = stack.pop()
                ans[job_id] += (ts - start_ts + 1) - delay
                if stack:
                    stack[-1][2] += (ts - start_ts + 1)
        return ans

print Solution().exclusiveTime(2,["0:start:0","1:start:2","1:end:5","0:end:6"])