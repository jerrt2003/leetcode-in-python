class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        ranks = dict()
        for vote in votes:
            for i, v in enumerate(vote):
                ranks.setdefault(v, [0]*len(vote))[i] -= 1
        return ''.join(sorted(ranks, key=lambda x: (ranks[x],x)))

print Solution().rankTeams(["ABC","ACB","ABC","ACB","ACB"])