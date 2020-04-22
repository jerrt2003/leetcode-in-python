class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        preOp = '+'
        num = 0
        for i, elem in enumerate(s):
            if elem.isdigit():
                num = 10*num + int(elem)
            if elem in '+-/*' or i == len(s)-1:
                if preOp == '+':
                    stack.append(num)
                elif preOp == '-':
                    stack.append(-num)
                elif preOp == '*':
                    stack.append(stack.pop()*num)
                else:
                    preNum = stack.pop()
                    if preNum < 0:
                        stack.append(-1 * (-1*preNum/num))
                    else:
                        stack.append(preNum/num)
                num = 0
                preOp = elem
        return sum(stack)

assert Solution().calculate("14-3/2") == 13