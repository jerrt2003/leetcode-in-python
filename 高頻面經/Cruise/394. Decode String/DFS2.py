# -*- coding: utf-8 -*-
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def dfs(idx):
            m = ''
            res = ''
            while idx < len(s):
                if s[idx] == ']':
                    return res, idx
                elif s[idx] == '[':
                    tmp_res, idx = dfs(idx+1)
                    res += int(m) * tmp_res
                    m = ''
                elif s[idx].isdigit():
                    m += s[idx]
                elif s[idx].isalpha():
                    res += s[idx]
                idx += 1
            return res, idx

        res, _ = dfs(0)
        return res

s = "3[a]2[bc]"
assert Solution().decodeString(s) == 'aaabcbc'