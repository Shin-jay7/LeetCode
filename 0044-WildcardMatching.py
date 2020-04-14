from __future__ import annotations


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        transfer = {}
        state = 0

        for char in p:
            if char == '*':
                transfer[state, char] = state
            else:
                transfer[state, char] = state+1
                state += 1
        # print(transfer)

        accept = state
        states = set([0])

        for char in s:
            next_states = set()
            for token in [char, '*', '?']:
                for at in states:
                    next_state = transfer.get((at, token))
                    if next_state != None:
                        next_states.add(next_state)

            states = next_states

        # print(states)

        # print(accept in states)
        return accept in states


test = Solution()
test.isMatch("aa", "a") # False

test = Solution()
test.isMatch("aa", "*") # True

test = Solution()
test.isMatch("cb", "?a") # False

test = Solution()
test.isMatch("adceb", "*a*b") # True

test = Solution()
test.isMatch("acdcb", "a*c?b") # False
