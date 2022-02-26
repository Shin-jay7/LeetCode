from __future__ import annotations
from typing import List
from collections import deque
from itertools import product


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
       
        bank, queue = set(bank), deque([(start, 0)])

        while queue:
            gene, cnt = queue.popleft()
            for i, char in product(range(len(start)), 'ACGT'):
                mutation = gene[:i] + char + gene[i+1:]
                if mutation in bank:
                    if mutation == end:
                        return cnt + 1

                    bank.remove(mutation)
                    queue.append((mutation, cnt+1))

        return -1


test = Solution()
test.minMutation("AACCGGTT", "AACCGGTA", [])
# -1

test = Solution()
test.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
# 1

test = Solution()
test.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"])
# 2

test = Solution()
test.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"])
# 3
