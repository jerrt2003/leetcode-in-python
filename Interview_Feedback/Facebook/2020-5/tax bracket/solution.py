# taxBracket = [[38700, .12], [9525, .10], [82500, .22], [157500, .24],[float('inf'), .32]]

class Solution(object):

    def calculateTax(self, brackets, income):
        brackets.sort(key=lambda x: x[0])
        # use binary search to get the idx of which range we should be in
        # l, r = 0, len(brackets)
        # while l < r:
        #     mid = (l+r-1)/2
        #     if brackets[mid][0] > income:
        #         r = mid
        #     else:
        #         l = mid+1
        tax = 0
        prevTaxableAmount = 0
        taxableIncome = 0

        for i in range(len(brackets)):
            taxableIncome, rate = brackets[i][0], brackets[i][1]
            if income > taxableIncome:
                tax += (taxableIncome - prevTaxableAmount) * rate
                prevTaxableAmount = taxableIncome
            else:
                tax += (income - prevTaxableAmount) * rate
                break

        return tax

print Solution().calculateTax([[38700, .12], [9525, .10], [82500, .22], [157500, .24],[float('inf'), .32]], 2000000)