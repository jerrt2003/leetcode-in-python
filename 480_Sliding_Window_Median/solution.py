from bisect import insort


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = sorted(nums[:k])

        def remove_num(target, window):
            l, r = 0, len(window)
            while l < r:
                mid = (l + r - 1) / 2
                if window[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return window[:l] + window[l + 1:]

        odd = k % 2
        if not odd:
            ans = [float((window[k / 2] + window[k / 2 - 1])) / 2]
        else:
            ans = [window[k / 2]]
        for i in range(k, len(nums)):
            j = i - k
            window = remove_num(nums[j], window)
            insort(window, nums[i])
            if not odd:
                ans.append(float((window[k / 2] + window[k / 2 - 1])) / 2)
            else:
                ans.append(window[k / 2])

        return ans


print Solution().medianSlidingWindow([1,2,3,4,2,3,1,4,2],3)
print Solution().medianSlidingWindow([1,4,2,3],4)