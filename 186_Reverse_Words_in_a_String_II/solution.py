class Solution(object):
    def reverseWords(self, s):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 236 ms, faster than 86.56% of Python online submissions for Reverse Words in a String II.
        Memory Usage: 21.7 MB, less than 45.16% of Python online submissions for Reverse Words in a String II.
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        def swap(x, y):
            while x < y:
                s[x], s[y] = s[y], s[x]
                x += 1
                y -= 1

        pt1, pt2 = 0, 0
        while pt2 < len(s):
            if s[pt2] == " ":
                swap(pt1, pt2 - 1)
                pt1 = pt2 = pt2 + 1
            else:
                pt2 += 1
        swap(pt1, pt2-1)


print Solution().reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])