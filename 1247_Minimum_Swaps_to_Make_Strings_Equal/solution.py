class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        Facebook
        T:O(n) S:O(1)
        https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/discuss/419874/Simply-Simple-Python-Solution-with-detailed-explanation
        :type s1: str
        :type s2: str
        :rtype: int
        """
        xy = yx = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    xy += 1
                else:
                    yx += 1

        if (xy + yx) % 2 == 1:
            return -1

        ans = xy / 2
        ans += yx / 2

        if xy % 2 == 1:
            ans += 2

        return ans