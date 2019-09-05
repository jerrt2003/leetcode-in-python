# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def isPossible(self, nums):
        """
        用freq map先过一遍存频率，再建一个map存我们能用到的tail number。再过第二遍的时候，若freq==0 continue；若能接上前面的顺子，
        就接；不能则新开一个顺子（记住新开时候直接要把连着的两个数字剔除，因为要保证长度为三）；都不行则为false。记住最后别忘了更新当前频率
        对于每一个element，我们有两种选择
            1. 把它加入之前构造好的顺子中
            2. 用它新开一个顺子
        此处用贪心策略，如果1能满足总是先满足1，因为新开顺子可能失败，即使新开顺子成功，当1能满足的时候，将新开顺子加入之前的顺子也能成功，
        所以能够选择策略1的时候没必要冒风险选择策略2
        目标是用策略1或者2消耗掉所有的元素
        如果两个策略都无法选择，直接返回false
        用另一个map记录已经构造好的顺子中现在需要哪些尾巴，来实现将当前元素加入构造好的顺子中

        T: O(n)
        S: O(n)
        Perf: Runtime: 620 ms, faster than 49.43% / Memory Usage: 12.8 MB, less than 82.43%
        :type nums: List[int]
        :rtype: bool
        """
        freq = hash2.Counter(nums)
        tail = hash2.Counter()
        for x in nums:
            if freq[x] == 0:
                continue
            elif tail[x] > 0:
                tail[x] -= 1
                tail[x+1] += 1
            elif freq[x+1] > 0 and freq[x+2] > 0:
                freq[x+1] -= 1
                freq[x+2] -= 1
                tail[x+3] += 1
            else:
                return False
            freq[x] -= 1
        return True