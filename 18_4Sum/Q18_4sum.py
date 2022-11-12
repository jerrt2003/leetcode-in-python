__author__ = 'dcheng'
class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        answerList = []
        for i in range(len(nums)):
            n1 = nums[i]
            newTarget = target - n1
            n2_nums = nums[i+1:]
            for j in range(len(n2_nums)):
                n2 = n2_nums[j]
                finalTarget = newTarget - n2
                start = j+1
                end = len(n2_nums)-1
                while not start >= end:
                    if n2_nums[start] + n2_nums[end] == finalTarget:
                        aList = []
                        aList.append(n1)
                        aList.append(n2)
                        aList.append(n2_nums[start])
                        aList.append(n2_nums[end])
                        if aList not in answerList:
                            answerList.append(aList)
                        start += 1
                    elif n2_nums[start] + n2_nums[end] < finalTarget:
                        start += 1
                    else:
                        end -= 1
        return answerList

sum = Solution()
'''
answer = sum.fourSum([5,5,3,5,1,-5,1,-2], 4)
print(answer)
'''
answer = sum.fourSum([0,4,-5,2,-2,4,2,-1,4], 12)
print(answer)

