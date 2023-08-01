import collections
import heapq


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # 建立一个字典，key为字符，value为该字符出现的下標的队列
        char_idx_list = collections.defaultdict(collections.deque)
        for i, c in enumerate(croakOfFrogs):
            char_idx_list[c].append(i)
        # 先判斷是否有不同字符的下標數量不一致，如果不一致，返回-1(i.e. 有不同字符的下標數量不一致，則無法組成croak)
        s = "croak"
        for i in range(1, len(s)):
            if len(char_idx_list[s[i]]) != len(char_idx_list[s[i - 1]]):
                return -1

        # pq儲存 'k'的下標 即 'corak'最後字符的下標
        pq = []
        while char_idx_list["c"]:
            # prev_idx為上一個字符的下標
            prev_idx = char_idx_list["c"].popleft()
            # 若 'c'的下標比pq中最小的下標還小(i.e. c 出現在'k'之後, 表示前面有一隻青蛙已經叫完了，可以重複利用)
            if pq and prev_idx > pq[0]:
                heapq.heappop(pq)
            for char in ["r", "o", "a", "k"]:
                # 若char的下標比prev_idx小 返回-1
                # e.g. "aoocrrackk"，第ㄧ個'a'的下標比第一個'o'的下標小
                if char_idx_list[char][0] < prev_idx:
                    return -1
                prev_idx = char_idx_list[char].popleft()
            heapq.heappush(pq, prev_idx)

        return len(pq)
