from __future__ import annotations
from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = list(Counter(tasks).values())
        max_count = max(tasks_count)
        pattern = n + 1
        freq = max_count - 1
        max_count_tasks = tasks_count.count(max_count)
        return max(len(tasks), pattern * freq + max_count_tasks)
        # tasks = [A,A,A,B,B,B,C,C,D,D], n = 3
        # 
        # A_ _ _ A_ _ _ A
        # AB_ _ AB_ _ AB
        # ABC_ ABC_ AB
        # ABCD ABCD AB
        # 
        # A_ _ _ x 2 + AB = pattern x freq + max_count_tasks
