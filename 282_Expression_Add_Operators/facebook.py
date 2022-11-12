class Solution(object):
    def addOperators(self, num, target):
        """
        Facebook
        Backtracking
        T:O(n) S:O(n)
        Runtime: 1404 ms, faster than 30.28% of Python online submissions for Expression Add Operators.
        Memory Usage: 13.2 MB, less than 15.00% of Python online submissions for Expression Add Operators.
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []

        def dfs(total, idx, path, last_num):
            if idx == len(num) and total == target:
                ans.append(path)
                return
            for i in range(idx + 1, len(num) + 1):
                curr_num = num[idx:i]
                if len(curr_num) == 1 or (len(curr_num) > 1 and curr_num[0] != '0'):
                    curr_num = int(curr_num)
                    dfs(total + curr_num, i, path + '+' + str(curr_num), curr_num)
                    dfs(total - curr_num, i, path + '-' + str(curr_num), -curr_num)
                    dfs(total - last_num + last_num * curr_num, i, path + '*' + str(curr_num), last_num * curr_num)

        for i in range(1, len(num)+1):
            if len(num[:i]) == 1 or num[:i][0] != '0':
                dfs(int(num[:i]), i, num[:i], int(num[:i]))

        return ans
        # ans = []
        # DP = set()
        #
        # def dfs(i, total, path, prev):
        #     if i == len(num) and total == target:
        #         ans.append(path)
        #         return True
        #     elif i == len(num):
        #         return False
        #     if (i, total) in DP:
        #         return False
        #     for j in range(i + 1, len(num) + 1):
        #         curr = num[i:j]
        #         if len(curr) == 1 or (len(curr) > 1 and curr[0] != '0'):
        #             a = dfs(j, total + int(curr), path + "+" + curr, int(curr))
        #             b = dfs(j, total - int(curr), path + "-" + curr, -int(curr))
        #             c = dfs(j, total - prev + prev * int(curr), path + "*" + curr, prev * int(curr))
        #             if not a and not b and not c:
        #                 DP.add((i, total))
        #                 return False
        #             return True
        #
        # for i in range(1, len(num) + 1):
        #     if len(num[:i]) == 1 or (len(num[:i]) > 1 and num[:i][0] != '0'):
        #         dfs(i, int(num[:i]), num[:i], int(num[:i]))
        #
        # return ans


print Solution().addOperators('123', 6)
# print Solution().addOperators('105', 5)
# print Solution().addOperators("000", 0)