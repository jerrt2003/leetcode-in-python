# class Solution(object):
#     def multiply(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         c2int_maps = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
#         ans = 0
#         for i, c1 in enumerate(num1[::-1]):
#             for j, c2 in enumerate(num2[::-1]):
#                 ans += c2int_maps[c1] * c2int_maps[c2] * (10 ** (i+j))
#         return str(ans)


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                curr = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                total = curr + res[p2]
                res[p1] += total / 10
                res[p2] = total % 10

        res = ''.join(str(num) for num in res)
        zero_position = 0
        while zero_position < len(res)-1 and res[zero_position] == '0':
            zero_position += 1
        return res[zero_position:]


print Solution().multiply("123","456")