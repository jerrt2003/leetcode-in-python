class Solution(object):
    def calculate(self, s):
        """
        Facebook
        Stack
        T:O(n) S:O(n)
        Runtime: 188 ms, faster than 31.41% of Python online submissions for Basic Calculator II.
        Memory Usage: 15 MB, less than 63.04% of Python online submissions for Basic Calculator II.
        :type s: str
        :rtype: int
        """
        ans = []
        num = 0
        sign = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                num = num*10 + int(c)
            if (not c.isdigit() and c != " ") or i == len(s)-1:
                if sign == "+":
                    ans.append(num)
                elif sign == "-":
                    ans.append(-num)
                elif sign == "*":
                    ans.append(num*ans.pop())
                else:
                    tmp = ans.pop()
                    if tmp < 0:
                        ans.append(-(abs(tmp)/num))
                    else:
                        ans.append(tmp/num)
                num = 0
                sign = c
        return sum(ans)


print Solution().calculate("14-3/2")