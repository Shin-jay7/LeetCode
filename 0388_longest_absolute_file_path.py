from __future__ import annotations


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        longest, dict = 0, {}
        for file in input.splitlines():
            depth = file.count("\t")
            if "." not in file:
                dict[depth] = len(file) - depth
            else:
                length = len(file) + sum([dict[i] for i in range(depth)])
                longest = max(longest, length)

        return longest
