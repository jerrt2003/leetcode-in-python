# -*- coding: utf-8 -*-
"""
第二道题:给两个string s1, s2. 将s1中的两个char交换一次，得到一个string，是否等于s2.
如果两个string相同，return false; 因为不能交换。
如果有一个char不同 return false; 因为不能交换。 . check 1point3acres for more.
如果有两个char不同，return 两个char换个位置是否等于s2。
如果有超过两个char不同，return false 因为一次交换肯定不能变成s2。
sample:
a != a, aa != aa, abc != cba -> 这些return false
abc = acb, converse=conserve -> 这些return true
"""
import hash2
class GoogleInterview(object):
    def Solution(self, s1, s2):
        s1_map = hash2.defaultdict(int)
        s2_map = hash2.defaultdict(int)

        m, n = len(s1), len(s2)
        if m != n or m == 1 or s1 == s2:
            return False
        diff_num = 0
        for i in range(m):
            s1_map[s1[i]] += 1
            s2_map[s2[i]] += 1
            if s1[i] != s2[i]:
                diff_num += 1

        if s1_map != s2_map or diff_num > 2:
            return False

        return True


#s1 = 'converse'
#s2 = 'conserve'

#s1 = 'cnoverse'
#s2 = 'conserve'


s1 = 'abc'
s2 = 'cab'



print GoogleInterview().Solution(s1, s2)