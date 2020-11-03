class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i > -1 and (backS > 0 or S[i] == '#'):
                if S[i] == '#':
                    backS += 1
                else:
                    backS -= 1
                i -= 1

            while j > -1 and (backT > 0 or T[j] == '#'):
                if T[j] == '#':
                    backT += 1
                else:
                    backT -= 1
                j -= 1

            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if S[i] != T[j]:
                return False
            i -= 1
            j -= 1


print Solution().backspaceCompare("ab##","c#d#")