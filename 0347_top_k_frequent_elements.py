from __future__ import annotations
from typing import List
from collections import Counter
from itertools import chain


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ans = []
        for num, _ in counter.most_common(k):
            ans.append(num)

        return ans
        # print(ans)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        counter = Counter(nums).items()
        for num, freq in counter:
            bucket[freq].append(num)
            
        flat_list = list(chain(*bucket))

        return flat_list[::-1][:k]
        # print(flat_list[::-1][:k])


test = Solution()
test.topKFrequent([1,1,1,2,2,3], 2) # [1, 2]

test = Solution()
test.topKFrequent([1], 1) # [1]
