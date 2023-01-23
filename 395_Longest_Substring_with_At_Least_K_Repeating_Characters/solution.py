import collections

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = -float('inf')
        # 题目说明了只包含小写字母（26 个，为有限数据），
        # 我们可以枚举最大长度所包含的字符类型数量，答案必然是 [1, 26]，
        # 即最少包含 1 个字母，最多包含 26 个字母。
        # 当确定了长度所包含的字符种类数量时，区间重新具有了二段性质
        # 当我们使用双指针的时候：
        # 1.右端点往右移动必然会导致字符类型数量增加（或不变）
        # 2.左端点往右移动必然会导致字符类型数量减少（或不变)
        # 当然，我们还需要记录有多少字符符合要求（出现次数不少于 k），
        # 当区间内所有字符都符合时更新答案。

        # char_limit == 區間內出現不同字符的量
        for char_limit in range(1, 27):
            # types_least_k: 區間內符合條件(即出現頻率不小於k)的字符數量
            # j：左pointer
            types_least_k, j = 0, 0
            # counters: 紀錄字符出現頻率的哈希表
            counters = collections.defaultdict(int)
            for i in range(len(s)):
                # 字符出現頻率+1
                counters[s[i]] += 1
                # 當字符出現頻率等於k時 將'區間內符合條件(即出現頻率不小於k)的字符數量'+1
                if counters[s[i]] == k:
                    types_least_k += 1
                # 當區間內字符類別數大於此迴圈的上限(char_limit)時 移動左pointer
                # 直到區間內字符類別數再次小於等於上限
                while len(counters.keys()) > char_limit:
                    counters[s[j]] -= 1
                    if counters[s[j]] == k-1:
                        types_least_k -= 1
                    if counters[s[j]] == 0:
                        del(counters[s[j]])
                    j += 1
                if types_least_k == len(counters.keys()):
                    ans = max(ans, i-j+1)
        return ans if ans != -float('inf') else 0
                
