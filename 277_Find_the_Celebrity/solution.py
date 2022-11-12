# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 1680 ms, faster than 35.15% of Python online submissions for Find the Celebrity.
        Memory Usage: 13.1 MB, less than 5.20% of Python online submissions for Find the Celebrity.
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i != candidate and (not knows(i, candidate) or knows(candidate, i)):
                return -1
        return candidate



