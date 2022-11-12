# -*- coding: utf-8 -*-
class Solution(object):
    def numDecodings(self, s):
        """
        DP: Bottom-Up solution
        Time Complexity:
        Space Complexity:
        Inspired by: leetcode.com/problems/decode-ways/discuss/30358/Java-clean-DP-solution-with-explanation/116646
        Thought:
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        len_s = len(s)
        DP = [0 for _ in range(len_s+1)] # DP[i]代表該位數的解碼數,DP[0]=0因為0無法解碼
        # 決定DP[1]的值
        DP[1] = 0 if int(s[0]) == 0 else 1
        if len_s == 1: return DP[1]
        if int(s[1]) != 0:
            DP[2] = DP[1]
        if 10 <= int(s[0:2]) <= 26:
            DP[2] += 1
        for i in range(3, len_s+1):
            if int(s[i-1]) != 0: # s[i-1]因為s從0開始 ＃若s[i-1]!=0的話總解碼數DP[i]=DP[i-1](上一組解碼數)因為總解碼數不變
                DP[i] = DP[i-1]
            if 10 <= int(s[i-2:i]) <= 26: # 考慮前兩位數, 若是前兩位在10~26, 則需加上其解碼組合數也就是DP[i-2]
                DP[i] += DP[i-2]
        return DP[len_s]

input = '100'
sol = Solution()
print sol.numDecodings(input)