from __future__ import annotations
from typing import List
from itertools import islice, product
from heapq import heappop, heappush, nsmallest, merge


# Time Limit Exceeded
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        return map(list, sorted(product(nums1, nums2), key=sum)[:k])
        

# Time Limit Exceeded
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        return map(list, nsmallest(k, product(nums1, nums2), key=sum))


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
        stream = merge(*streams)
        return [pair[1:] for pair in islice(stream, k)]


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(queue, [nums1[i]+nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j+1)
            if j == 0:
                push(i+1, 0)
        return pairs
