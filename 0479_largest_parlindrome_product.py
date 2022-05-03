from __future__ import annotations
from re import A


# Let Palindrome = X * Y, both have n digits, and assume they are very close to 10^n
# Denote X = 10^n - i, Y = 10^n - j, with assumption: i*j < 10^n
# Palindrome = upper * 10^n + lower = (10^n - i)(10^n - j) = (10^n - i - j) * 10^n + i * j
# therefore: upper = 10^n - i - j, lower = i * j
# Let a = i + j, upper = 10^n - a, lower = i * (a-i)
# Algorithm: we iterate a and search for an integer i
# -lower + lower = i^2 - a*i + lower = 0 => (i - a/2)^2 = i^2 - a*i + 0.25 * a^2 = 0.25 * a^2 - lower
# Given a start from 2, check if sqrt(a^2 - lower * 4) is an integer, 
# then return upper * 10^n + lower


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        a = 2
        while a < 10**n:
            upper = 10**n - a
            lower = int(str(upper)[::-1])
            if a**2 - lower * 4 >= 0 and (a**2 - lower * 4)**0.5 == int((a**2 - lower * 4)**0.5):
                return (upper * 10**n + lower) % 1337
            a += 1
