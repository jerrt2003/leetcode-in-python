from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # mono_queue 是一個monotone dequeue(單調雙向隊列)
        mono_queue: List[int] = []
        # ans 為最後答案
        ans: List[int] = []
        # 遍歷數組
        for i, v in enumerate(nums):
            # 維持mono_queue monotone的遞減性質
            # 當前遍歷數大於mono_queue的尾數時 pop mono_queue最尾數
            while mono_queue and v > nums[mono_queue[-1]]:
                mono_queue.pop()
            # 將idx push進mono_queue
            mono_queue.append(i)
            # 當 i >= k-1 即代表size為k的窗口形成
            if i >= k-1:
                # 將當前mono_queue首數加入ans
                # 由於monotone queue的特性 我們可以保證首數一定為該mono_queue最大值
                ans.append(nums[mono_queue[0]])
                # 當窗口向前滑移時,我們要確定即將離開窗口的數並不為mono_queue首數
                # 若為mono_queue首數要將其移出
                if i-k+1 == mono_queue[0]:
                    mono_queue.pop(0)
        return ans