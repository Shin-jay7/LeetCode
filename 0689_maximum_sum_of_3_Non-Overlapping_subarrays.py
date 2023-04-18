from __future__ import annotations
from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        best_one, best_two, best_three = 0, [0, k], [0, k, k*2]
        first_sum, second_sum, third_sum =\
            sum(nums[:k]), sum(nums[k:k*2]), sum(nums[k*2:k*3])
        best_one_sum, best_two_sum, best_three_sum =\
            first_sum, first_sum+second_sum, first_sum+second_sum+third_sum
        first_idx, second_idx, third_idx = 1, k+1, k*2+1

        while third_idx <= len(nums)-k:
            first_sum += nums[first_idx+k-1] - nums[first_idx-1]
            second_sum += nums[second_idx+k-1] - nums[second_idx-1]
            third_sum += nums[third_idx+k-1] - nums[third_idx-1]

            if first_sum > best_one_sum:
                best_one_sum = first_sum
                best_one = first_idx

            if first_sum + second_sum > best_two_sum:
                best_two_sum = first_sum + second_sum
                best_two = [best_one, second_idx]

            if first_sum + second_sum + third_sum > best_three_sum:
                best_three_sum = first_sum + second_sum + third_sum
                best_three = [best_one, best_two[1], third_idx]

            first_idx += 1
            second_idx += 1
            third_idx += 1

        return best_three
