from __future__ import annotations


one_digit = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1,
             '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
tow_digits = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1,
              '15': 1, '16': 1, '17': 1, '18': 1, '19': 1,
              '20': 1, '21': 1, '22': 1, '23': 1, '24': 1,
              '25': 1, '26': 1,
              '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2, 
              '*5': 2, '*6': 2, '*7': 1, '*8': 1, '*9': 1,
              '1*': 9, '2*': 6, '**': 15}


class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = (1, one_digit.get(s[0], 0))
        for i in range(1, len(s)):
            dp = (dp[1],
                  (
                    one_digit.get(s[i], 0) * dp[1] +
                    tow_digits.get(s[i-1:i+1], 0) * dp[0]
                  ) % MOD)
        return dp[1]


class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        one_digit, two_digits_1x, two_digits_2x = 1, 0, 0
        for ch in s:
            if ch == '*':
                one_digit, two_digits_1x, two_digits_2x =\
                 (9 * one_digit +
                  9 * two_digits_1x +
                  6 * two_digits_2x) % MOD,\
                 one_digit, one_digit
            else:
                one_digit, two_digits_1x, two_digits_2x =\
                 ((ch > '0') * one_digit +
                  two_digits_1x +
                  (ch < '7') * two_digits_2x) % MOD,\
                 one_digit if ch == '1' else 0,\
                 one_digit if ch == '2' else 0
        return one_digit


test = Solution()
test.numDecodings('*')  # 9

test = Solution()
test.numDecodings('1*')  # 18

test = Solution()
test.numDecodings('2*')  # 15

test = Solution()
test.numDecodings('2**')  # 150
