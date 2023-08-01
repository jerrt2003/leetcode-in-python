class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur_sign = "+"
        cur_num = 0
        # 最末尾加一個'哨兵'
        for c in s + "+":
            if c.isdigit():
                cur_num = 10 * cur_num + (ord(c) - ord("0"))
            elif c in ["+", "-", "*", "/"]:
                if cur_sign == "+":
                    stack.append(cur_num)
                elif cur_sign == "-":
                    stack.append(cur_num * -1)
                elif cur_sign == "*":
                    pre_num = stack.pop()
                    stack.append(pre_num * cur_num)
                else:
                    pre_num = stack.pop()
                    stack.append(
                        -1 * (-1 * pre_num // cur_num)
                        if pre_num < 0
                        else pre_num // cur_num
                    )
                cur_num = 0
                cur_sign = c
        # 處理最後一個數字
        # if cur_num != 0:
        #     if cur_sign == "+":
        #         stack.append(cur_num)
        #     elif cur_sign == "-":
        #         stack.append(cur_num * -1)
        #     elif cur_sign == "*":
        #         pre_num = stack.pop()
        #         stack.append(pre_num * cur_num)
        #     else:
        #         pre_num = stack.pop()
        #         stack.append(
        #             -1 * (-1 * pre_num // cur_num)
        #             if pre_num < 0
        #             else pre_num // cur_num
        #         )

        return sum(stack)
