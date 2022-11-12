import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        Facebook
        Array
        T:O(nk) S:O(n)
        Runtime: 104 ms, faster than 49.69% of Python online submissions for Group Anagrams.
        Memory Usage: 18.7 MB, less than 5.36% of Python online submissions for Group Anagrams.
        !! Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            group[tuple(count)].append(s)
        return [v for v in group.values()]