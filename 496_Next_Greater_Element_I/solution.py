from typing import Dict, List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_ref: Dict[int, int] = {}
        stack = []
        for i, v in enumerate(nums2):
            while stack and v > nums2[stack[-1]]:
                idx = stack.pop()
                next_greater_ref[nums2[idx]] = v
            stack.append(i)

        ans = [-1 for _ in range(len(nums1))]
        for i, v in enumerate(nums1):
            if v in next_greater_ref.keys():
                ans[i] = next_greater_ref[v]

        return ans


# CHATGPT
# from typing import Dict, List

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         next_greater_ref: Dict[int, int] = {}
#         stack = []
#         for v in nums2:
#             while stack and v > stack[-1]:
#                 num = stack.pop()
#                 next_greater_ref[num] = v
#             stack.append(v)

#         return [next_greater_ref.get(num, -1) for num in nums1]
