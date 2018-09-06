class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = list()
        shift = 0
        for i in range(num+1):
            if i == 0:
                result.append(0)
            elif i == 1:
                result.append(1)
            elif (2 << shift) < i:
                shift += 1
            elif (2 << shift) == i:
                shift += 1
                result.append(1)
            else:
                tmp = 1 + result[i - (2 << shift-1)]
                result.append(tmp)
        return result

a = 9
sol = Solution()
print sol.countBits(a)