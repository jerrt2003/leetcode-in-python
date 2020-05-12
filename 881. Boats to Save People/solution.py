class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        2-pointer
        T:O(nlog(n)) S:O(n)
        Runtime: 452 ms, faster than 61.11% of Python online submissions for Boats to Save People.
        Memory Usage: 18.2 MB, less than 50.00% of Python online submissions for Boats to Save People.
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i, j = 0, len(people)-1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans