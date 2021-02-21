from __future__ import annotations


class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]


class Solution:
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        for i in range(k):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[len(nums)-k]


class Solution:
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        length = len(nums)
        for i in range(length, length-k, -1):
            tmp = 0
            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return nums[length-k]


class Solution:
    def findKthLargest4(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)


class Solution:
    def findKthLargest5(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)
        for num in nums[k:]:
            heappushpop(heap, num)
        return heap[0]
