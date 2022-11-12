class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = [""]*(target+1)

        def dfs(target):
            if target == 0:
                return ""
            elif target < 0:
                return "0"
            elif dp[target] != "":
                return dp[target]
            else:
                dp[target] = "0"
                for i in range(1, 10):
                    curr = dfs(target - cost[i-1])
                    if curr != "0" and len(curr)+1 >= len(dp[target]):
                        dp[target] = str(i) + curr
            return dp[target]

        return dfs(target)




print(Solution().largestNumber([4,3,2,5,6,7,2,5,5],9))
print Solution().largestNumber([7,6,5,5,5,6,8,7,8],12)