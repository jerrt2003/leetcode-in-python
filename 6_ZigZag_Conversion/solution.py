class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # using a list of str to record each char
        # s = "leetcode" num = 2
        # ref[0] = "lecd"
        # ref[1] = "etoe"
        # ans == "lecdetoe"
        if numRows == 1:
            return s
        ref = ["" for _ in range(numRows)]
        cur_row, flag = 0, -1
        for chr in s:
            ref[cur_row] += chr
            if cur_row == numRows - 1 or cur_row == 0:
                flag = flag * -1
            cur_row += flag
        return "".join(ref)