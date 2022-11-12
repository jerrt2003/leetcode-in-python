class Solution(object):
    def alphabetBoardPath(self, target):
        """
        T:O(n) S:O(n)
        Runtime: 20 ms, faster than 74.24% of Python online submissions for Alphabet Board Path.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Alphabet Board Path.
        :type target: str
        :rtype: str
        """
        graph = dict()
        for c in range(ord('a'),ord('z')+1):
            graph[chr(c)] = ((c-ord('a'))/5,((c-ord('a'))%5))
        pos = (0, 0)
        ans = []
        for c in target:
            s = ''
            x, y = graph[c][0]-pos[0], graph[c][1]-pos[1]
            if y < 0: s += 'L'*abs(y)
            if x < 0: s += 'U'*abs(x)
            if x > 0: s += 'D'*x
            if y > 0: s += 'R'*y
            ans.append(s+'!')
            pos = graph[c]
        return ''.join(ans)

print Solution().alphabetBoardPath('zdz')