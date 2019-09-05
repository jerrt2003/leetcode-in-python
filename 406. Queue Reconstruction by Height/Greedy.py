# -*- coding: utf-8 -*-
class Solution(object):
    def reconstructQueue(self, people):
        """
        Solution: Greedy..?!
        Time Complexity: O(n)
        Space Complexity: O(3n)
        Inspired By: https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89345/Easy-concept-with-PythonC++Java-Solution
        TP:
        - Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
        - For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
            E.g.
                input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
                subarray after step 1: [[7,0], [7,1]]
                subarray after step 2: [[7,0], [6,1], [7,1]]
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        import hash2
        people_dict = hash2.defaultdict(list)
        height = set()
        res = []
        for p in people:
            people_dict[p[0]].append(p)
            height.add(p[0])
        height = list(height)
        height.sort(reverse=True)
        for h in height:
            people_sub_group = people_dict[h]
            people_sub_group.sort()
            for p in people_sub_group:
                res.insert(p[1], p)
                '''
                WHY res.insert(p[1],p)..?
                Consider this case:
                subarray after step 1: [[7,0], [7,1]]
                --> the next step the height will be 6 and our condition is: where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h
                next height is 6 and its member is (6, 1) which means only one element in front of it has greater or equal to its height.
                thus we can simply insert it to position 1 to meet the condition. rest of the operation can follow the same routine
                '''
        return res

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print Solution().reconstructQueue(people)