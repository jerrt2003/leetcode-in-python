import math
class Solution():
    INT_MAX = int(math.pow(2,31) - 1)
    INT_MIN = int(-math.pow(2,31))
    def myAtoi(self, str):
        """
        To convert string to integer
        :param str:
        :return: int
        """
        if len(str) == 0: return 0
        tmp_str = str.strip()
        if len(tmp_str) == 0: return 0
        if tmp_str[0].isalpha(): return 0
        sign = -1 if tmp_str[0] == '-' else 1
        if tmp_str[0] in ['-','+']:
            tmp_str = tmp_str[1:]
        result = 0
        i = 0
        while i < len(tmp_str):
            if not tmp_str[i].isdigit():
                break
            else:
                result = result*10 + int(tmp_str[i])
            i += 1
        if sign == -1:
            return max(self.INT_MIN, -1*result)
        else:
            return min(self.INT_MAX, result)

test_int = [' ','42', '    -42', '4193 with words', 'words and 987', '-91283472332']
sol = Solution()
for i in test_int:
    print sol.myAtoi(i)