from __future__ import annotations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i,v in enumerate(nums):
            complement = target - v
            if complement not in lookup:
                lookup[v] = i
            else:
                return [lookup[complement], i]

# import timeit

# code = """
# class Solution:
#     def twoSum(self, nums, target):
#         lookup = {}
#         for i,v in enumerate(nums):
#             complement = target - v
#             if complement not in lookup:
#                 lookup[v] = i
#             else:
#                 return [lookup[complement], i]

# test = Solution()
# nums = [2, 7, 11, 15]
# test.twoSum(nums, 9)
# """

# print(timeit.timeit(code, number=10000))


