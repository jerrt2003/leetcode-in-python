class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = [None]*(target+1)

        def buildDP(curr_target):
            if curr_target < 0:
                return None
            elif curr_target == 0:
                return ""
            elif dp[curr_target]:
                return dp[curr_target]
            else:
                for i in range(1, 10):
                    nxt = buildDP(curr_target - cost[i-1])
                    if not nxt and len(nxt)+1 >= len(dp[curr_target]):
                        dp[curr_target] = str(i) + nxt
                return dp[curr_target]

        return buildDP(target)

print(Solution().largestNumber([4,3,2,5,6,7,2,5,5],9))