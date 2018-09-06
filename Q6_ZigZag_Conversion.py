class Solution():
    def convert(self, s, numRows):
        """
        To covert ZigZag Conversation
        :param s:
        :param numRows:
        :return:
        """
        if numRows == 1 or len(s) < numRows:
            return s

        res = [''] * numRows
        idx = 0
        step = 1
        for x in s:
            res[idx] += x
            if idx == 0:
                step = 1
            elif idx == numRows -1:
                step = -1
            idx += step
        return ''.join(res)


s = 'PAYPALISHIRING'
rows = 3
c = Solution()
print c.convert(s, rows)