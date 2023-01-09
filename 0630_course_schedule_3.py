from __future__ import annotations
from typing import List
from heapq import heappush, heappop


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        start, valid_list = 0, []
        for time, end in sorted(courses, key=lambda x: x[1]):
            if start + time <= end:
                valid_list.append(time)
                start += time
            else:
                max_idx = 0
                for idx in range(1, len(valid_list)):
                    if valid_list[idx] > valid_list[max_idx]:
                        max_idx = idx
                if valid_list and valid_list[max_idx] > time:
                    start += time - valid_list[max_idx]
                    valid_list[max_idx] = time
        return len(valid_list)


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        queue, start = [], 0
        for time, end in sorted(courses, key=lambda x: x[1]):
            start += time
            heappush(queue, -time)
            if start > end:
                start += heappop(queue)
        return len(queue)


test = Solution()
test.scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]])  # 3

test = Solution()
test.scheduleCourse([[1,2]])  # 1

test = Solution()
test.scheduleCourse([[3,2],[4,3]])  # 0
