from __future__ import annotations
from typing import List


class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        self.memo = {}

        def find_lowest_cost(needs):
            if tuple(needs) in self.memo:
                return self.memo[tuple(needs)]
            cost = 0
            for i, need in enumerate(needs):
                cost += need * price[i]
            for offer in special:
                for i, need in enumerate(needs):
                    if need < offer[i]:
                        break
                    else:
                        new_needs = [
                             need - offer[i] for i, need in enumerate(needs)
                            ]
                        cost = min(cost,
                                   offer[-1] + find_lowest_cost(new_needs)
                                   )
            self.memo[tuple(needs)] = cost
            return cost

        return find_lowest_cost(needs)
