# -*- coding: utf-8 -*-
class Solution(object):
    def findItinerary(self, tickets):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!!
        TP:
        - a DFS solution
        - first we sort the tickets using "dst" as key (so we can have lexical order)
        - then we filter out all possible tickets start @ 'JFK' and put its idx into a list
        - then we go through the list one by one to find possible answer
        - for each level of recursion, we will pass in: 1. current itenerary 2. ticket left then we do:
            - find out the last stop: current_itenerary[-1]
            - for tickets left find out all possible tickets idx
            - for each possible tickets we do same recursion:
                - pop ticket(idx) to get tickets_left
                - add this tickets to current itenerary
                - pass those into recursion again
                - if len(tickets_left) == 0 which means there are no more tickets left, then we are done.
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets.sort(key=self.getKey)
        candidates = []
        for i in range(len(tickets)):
            if tickets[i][0] == "JFK":
                candidates.append(i)
        for candidate in candidates:
            tickets_left = tickets[:]
            tmp = tickets_left.pop(candidate)
            itenerary = [tmp[0],tmp[1]]
            res = self.build(itenerary, tickets_left)
            if res[0]:
                return res[1]
        return []

    def build(self, itenerary, tickets_left):
        if len(tickets_left) == 0:
            return True, itenerary
        last_stop = itenerary[-1]
        candidates = []
        for i in range(len(tickets_left)):
            if tickets_left[i][0] == last_stop:
                candidates.append(i)
        for candidate in candidates:
            tmp = tickets_left[:]
            ticket = tmp.pop(candidate)
            tmp_itenerary = itenerary[:]
            tmp_itenerary.append(ticket[1])
            res = self.build(tmp_itenerary, tmp)
            if res[0]:
                return True, res[1]
        return False, []

    def getKey(self, elem):
        return elem[1]


#tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#tickets = [["JFK","ATL"],["ATL","JFK"]]
tickets = [["JFK","SFO"]]
#tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
#tickets = []
sol = Solution()
print sol.findItinerary(tickets)