from __future__ import annotations


class Solution: deserialize=eval


class Solution:
    def deseiralize(self, s: str) -> NestedInteger:
        def nested_integer(chars):
            if isinstance(chars, int):
                return NestedInteger(chars)
            lst = NestedInteger()
            for char in chars:
                lst.add(nestedInteger(char))
            return lst
        return nested_integer(eval(s))


