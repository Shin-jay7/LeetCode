from __future__ import annotations
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans, _sum = [], float('inf')
        for idx, word in enumerate(list1):
            if word in list2:
                cur = idx + list2.index(word)
                if cur < _sum:
                    _sum = cur
                    ans = [word]
                elif cur == _sum:
                    ans.append(word)

        return ans


test = Solution()  # ["Shogun"]
test.findRestaurant(
     ["Shogun", "Tapioca Express", "Burger King", "KFC"],
     ["Piatti", "The Grill at Torrey Pines",
      "Hungry Hunter Steakhouse", "Shogun"]
    )

test = Solution()  # ["Shogun"]
test.findRestaurant(
     ["Shogun", "Tapioca Express", "Burger King", "KFC"],
     ["KFC", "Shogun", "Burger King"]
    )

test = Solution()  # ["sad","happy"]
test.findRestaurant(
     ["happy", "sad", "good"], ["sad", "happy", "good"]
    )

test = Solution()  # ["Piatti"]
test.findRestaurant(
     ["Shogun", "Piatti", "Tapioca Express", "Burger King", "KFC"],
     ["Piatti", "The Grill at Torrey Pines",
      "Hungry Hunter Steakhouse", "Shogun"]
    )
