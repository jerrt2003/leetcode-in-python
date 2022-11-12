import collections


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        BS
        T:O(n) S:O(n)
        :type persons: List[int]
        :type times: List[int]
        """
        lead = -1
        self.lead = []
        count = collections.defaultdict(int)
        self.times = times
        for p in persons:
            count[p] += 1
            if not lead or count[p] >= count[lead]:
                lead = p
            self.lead.append(lead)

    def q(self, t):
        """
        T:O(log(n))
        :type t: int
        :rtype: int
        """
        l, r = 0, len(self.times)
        while l < r:
            m = (l+r-1)/2
            if self.times[m] > t:
                r = m
            else:
                l = m+1
        return self.lead[l-1]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)