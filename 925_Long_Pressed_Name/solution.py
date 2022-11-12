class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        # if len(name) > len(typed):
        #     return False
        # i, j = 0, 0
        # while i < len(name) and j < len(typed):
        #     if name[i] == typed[j]:
        #         i += 1
        #         j += 1
        #     elif name[i] != typed[j] and i == 0 and j == 0:
        #         return False
        #     elif name[i] != typed[j] and typed[j] == typed[j-1]:
        #         j += 1
        #     else:
        #         return False
        # if i < len(name):
        #     return False
        # while j < len(typed):
        #     if typed[j] == typed[j-1]:
        #         j += 1
        #     else:
        #         return False
        # return True
        i, j = 0, 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
        return i == len(name)

print Solution().isLongPressedName("pyplrz","ppyypllr")