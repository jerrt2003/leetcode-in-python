import collections


class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nxt = collections.defaultdict(list)
        for i, v in enumerate(arr):
            nxt[v].append(i)
        visit = [False for _ in range(len(arr))]
        queue = [len(arr)-1]
        count = 0
        while queue:
            nxt_queue = []
            while len(queue) != 0:
                curr_idx = queue.pop(0)
                if curr_idx == 0:
                    return count
                if not visit[curr_idx]:
                    visit[curr_idx] = True
                    nxt_queue += nxt[arr[curr_idx]]
                    if curr_idx-1 >= 0:
                        nxt_queue.append(curr_idx-1)
                    if curr_idx+1 < len(arr):
                        nxt_queue.append(curr_idx+1)
            queue = nxt_queue
            count += 1

print Solution().minJumps([100,-23,-23,404,100,23,23,23,3,404])
print Solution().minJumps([7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,11])