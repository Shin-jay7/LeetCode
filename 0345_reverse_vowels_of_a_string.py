from __future__ import annotations
import re


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = 'aeiouAEIOU'
        left, right = 0, len(s)-1
        while left <= right:
            while left <= right and s[left] not in vowels:
                left += 1
            while left <= right and s[right] not in vowels:
                right -= 1
            if left > right:
                break
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)



# (?i) is an inline flag corresponding to re.IGNORECASE. In other words (?i)[aeiou] is equivalent to [aeiouAEIOU].
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda x: vowels.pop(), s)


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = (char for char in reversed(s) if char in 'aeiouAEIOU')
        return re.sub('(?i)[aeiou]', lambda x: next(vowels), s)
        