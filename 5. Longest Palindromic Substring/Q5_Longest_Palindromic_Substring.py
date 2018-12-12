import traceback
class Solution():
    def longestPalindrome(self, s):
        """
        to find longestPalindrome substring
        :param s:
        :return:
        """
        if len(s) < 2:
            return s
        result = ''
        for i in range(len(s)):
            if len(result) == 0:
                result = s[i]
            # all same word
            '''
            tmp = s[i]
            tmp_head = i+1
            while tmp_head < len(s):
                if s[i] == s[tmp_head]:
                    tmp += s[i]
                    if len(tmp) >= len(result):
                        result = tmp
                    tmp_head += 1
                else:
                    break
            '''
            # complete mirror
            idx_a = i
            idx_b = i + 1
            tmp = ''
            while idx_a >= 0 and idx_b < len(s):
                if s[idx_a] == s[idx_b]:
                    tmp = s[idx_a] + tmp + s[idx_b]
                    if len(tmp) >= len(result):
                        result = tmp
                    idx_a -= 1
                    idx_b += 1
                else:
                    break

            # center mirror
            tmp = s[i]
            head = i - 1
            tail = i + 1
            while head >= 0 and tail < len(s):
                if s[head] == s[tail]:
                    tmp = s[head] + tmp + s[tail]
                    if len(tmp) >= len(result):
                        result = tmp
                    head -= 1
                    tail += 1
                else:
                    break
        return result

s = "aaa"
c = Solution()
print c.longestPalindrome(s)