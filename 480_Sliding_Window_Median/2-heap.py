from heapq import *
class SolutionHeap(object):
    def medianSlidingWindow(self, nums, k):
        lh,rh,rv = [],[],[]
        # create the initial left and right heap
        for i,n in enumerate(nums[:k]): heappush(lh, (-n,i))
        for i in range(k-k/2):
            heappush(rh, (-lh[0][0], lh[0][1]))
            heappop(lh)
        for i,n in enumerate(nums[k:]):
            rv.append(rh[0][0]/1. if k%2 else (rh[0][0] - lh[0][0])/2.)
            if n >= rh[0][0]:
                heappush(rh,(n,i+k))        # rh +1
                if nums[i] <= rh[0][0]:     # lh-1, unbalanced
                    heappush(lh, (-rh[0][0], rh[0][1]))
                    heappop(rh)
                # else: pass                # rh-1, balanced
            else:
                heappush(lh,(-n,i+k))        # rh +1
                if nums[i] >= rh[0][0]:     # rh-1, unbalanced
                    heappush(rh, (-lh[0][0], lh[0][1]))
                    heappop(lh)
                # else: pass                # lh-1, balanced
            while(lh and lh[0][1] <= i): heappop(lh)  # lazy-deletion
            while(rh and rh[0][1] <= i): heappop(rh)  # lazy-deletion
        rv.append(rh[0][0]/1. if k%2 else (rh[0][0] - lh[0][0])/2.)
        return rv

print SolutionHeap().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3)