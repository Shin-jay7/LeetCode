from __future__ import annotations


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        seen = {}

        def can_win(choices, remainder):
            # if the largest choice exceeds the remainder, then we can win!
            if choices[-1] >= remainder:
                return True
            # if we have seen this exact scenario play out,
            # then we know the outcome
            seen_key = tuple(choices)
            if seen_key in seen:
                return seen[seen_key]
            # we haven't won yet.. it's the next player's turn.
            for idx in range(len(choices)):
                if not can_win(
                    choices[:idx] + choices[idx+1:], remainder - choices[idx]
                   ):
                    seen[seen_key] = True
                    return True
            # if we got here then next player won all permutations, we can't
            # force their hand actually, they were able to force our hand :(
            seen[seen_key] = False
            return False

        summed_choices = (maxChoosableInteger + 1) * maxChoosableInteger // 2
        # if all the choices added up are less then the total, no-one can win
        if summed_choices < desiredTotal:
            return False
        # if the sum matches desiredTotal exactly then you win 
        # if there's an odd number of turns
        if summed_choices == desiredTotal:
            return maxChoosableInteger % 2
        # go through the tree of permutations
        choices = list(range(1, maxChoosableInteger + 1))
        return can_win(choices, desiredTotal)
