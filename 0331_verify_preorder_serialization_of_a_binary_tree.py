from __future__ import annotations


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for char in preorder.split(","):
            stack.append(char)
            while len(stack) > 2 and stack[-2:] == ["#"]*2 and stack[-3] != "#":
                stack.pop(-3)
                stack.pop(-2)

        return stack == ["#"]
