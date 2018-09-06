class Solution():
    def intToRoman(self, num):
        """
        to convert int to Roman.
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        :param num:
        :return: string
        """
        num_list = list()
        digit_list = [1000,100,10,1]
        for digit in digit_list:
            _rem = num / digit
            num_list.append(_rem)
            num -= digit * _rem
        _convert = (('C','D','M'),('X','L','C'),('I','V','X'))
        result = ''
        for i in range(len(num_list)):
            if i == 0:
                result = result.join(num_list[i]*'M')
            else:
                if num_list[i] == 0:
                    continue
                elif 0 < num_list[i] < 4:
                    tmp_result = _convert[i-1][0] * num_list[i]
                elif num_list[i] == 4:
                    tmp_result = _convert[i-1][0] + _convert[i-1][1]
                elif num_list[i] == 5:
                    tmp_result = _convert[i-1][1]
                elif 5 < num_list[i] < 9:
                    tmp_result = _convert[i-1][1] + _convert[i-1][0]*(num_list[i]-5)
                else:
                    tmp_result = _convert[i-1][0] + _convert[i-1][2]
                result = result + tmp_result
        return result


test = 3
sol = Solution()
print sol.intToRoman(test)