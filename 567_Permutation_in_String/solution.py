import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = collections.Counter(s1)
        l, r = 0, len(s1)-1
        counter2 = collections.Counter(s2[l, r])
        while r < len(s2):
            counter2[s2[r]] += 1
            if counter1 == counter2:
                return True
            counter2[s2[l]] -= 1
            if counter2[s2[l]] == 0:
                del counter2[s2[l]]
            l += 1
            r += 1
        return False
