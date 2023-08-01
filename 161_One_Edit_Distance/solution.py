class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            return self.replace(s, t)
        if len(s) > len(t):
            return self.delete_by_one(s, t)
        else:
            return self.delete_by_one(t, s)

    def replace(self, w1, w2):
        diff = 0
        for a, b in zip(w1, w2):
            if a != b:
                diff += 1
        return diff == 1

    def delete_by_one(self, long, short):
        for i in range(len(long)):
            if long[:i] + long[i + 1 :] == short:
                return True
        return False
