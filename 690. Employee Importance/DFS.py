# -*- coding: utf-8 -*-
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        TP: MySELF!!
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        e_map = {e.id: e for e in employees}
        def find(id):
            importance = e_map[id].importance
            if len(e_map[id].subordinates) != 0:
                for e in e_map[id].subordinates:
                    importance += find(e.id)
            return importance
        return find(id)

