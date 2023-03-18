import collections

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # use a hashmap to store the char and its count
        counter = collections.defaultdict(int)
        j = 0
        ans = -float('inf')
        for i, c in enumerate(s):
            # increase the count of the char by 1
            counter[c] += 1
            # if the length of the hashmap is larger than k
            # we need to start move the left pointer to the right
            # so that the length of the hashmap is smaller/equal than k
            while len(counter.keys()) > k:
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    del(counter[s[j]])
                j+=1
            ans = max(i-j+1, ans)
        return ans