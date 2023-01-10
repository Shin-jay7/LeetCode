from __future__ import annotations
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans, stack, prev = [0] * n, [], 0
        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)
            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev
                stack.append(fn)
                prev = time
            else:
                ans[stack.pop()] += time - prev + 1
                prev = time + 1
        return ans


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans, stack = [0] * n, []
        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)
            if typ == 'start':
                stack.append(time)
            else:
                delta = time - stack.pop() + 1
                ans[fn] += delta
                stack = [time + delta for time in stack]
        return ans


test = Solution()
test.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])  # [3, 4]
