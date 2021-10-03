from __future__ import annotations


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {c: i for i, c in enumerate(s) }
        stack = ["#"]
        visited = set()

        for i, char in enumerate(s):
            if char in visited:
                continue
            while char < stack[-1] and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(char)
            visited.add(char)

        return "".join(stack)[1:]


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans = ''
        while s:
            i = min(map(s.rindex, set(s)))
            char = min(s[:i+1])
            ans += char
            s = s[s.index(char):].replace(char, '')
        return ans


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''


