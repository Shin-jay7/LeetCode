from __future__ import annotations


# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         candies = [1]*n
#         flag = True

#         while flag:
#             flag = False
#             for i in range(1,n-1):
#                 if ratings[i] > ratings[i-1] and\
#                    candies[i] <= candies[i-1]:
#                     candies[i] = candies[i-1]+1
#                     flag = True
#                 if ratings[i] > ratings[i+1] and\
#                    candies[i] <= candies[i+1]:
#                     candies[i] = candies[i+1]+1
#                     flag = True


#         return sum(candies)
#         # print(sum(candies))


# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         total, n = 0, len(ratings)
#         left2right, right2left = [1]*n, [1]*n

#         for i in range(1,n):
#             if ratings[i] > ratings[i-1]:
#                 left2right[i] = left2right[i-1] + 1

#         for i in range(n-2,-1,-1):
#             if ratings[i] > ratings[i+1]:
#                 right2left[i] = right2left[i+1] + 1

#         for i in range(n):
#             total += max(left2right[i], right2left[i])

#         return total
#         # print(total)


# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         candies = [1]*n

#         for i in range(1,n):
#             if ratings[i] > ratings[i-1]:
#                 candies[i] = candies[i-1] + 1

#         total = candies[-1]

#         for i in range(n-2,-1,-1):
#             if ratings[i] > ratings[i+1]:
#                 candies[i] = max(candies[i], candies[i+1]+1)
#             total += candies[i]

#         return total
#         # print(total)


class Solution:
    """
    in order to distribute the candies as per the given criteria
    using the minimum number of candies, the candies are always
    distributed in terms of increments of 1. Further, while
    distributing the candies, the local minimum number of candies
    given to a student is 1. Thus, the sub-distributions always
    take the 1, 2, 3, ..., n or n,..., 2, 1, whose sum is simply
    given by n(n+1)/2n(n+1)/2.
    """
    def cnt(sel, num):
        return num*(num+1)//2

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1: return n
        candies, up, dwn, prevSlope = 0, 0, 0, 0

        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                curSlope = 1
            elif ratings[i] < ratings[i-1]:
                curSlope = -1
            else:
                curSlope = 0

            if (prevSlope > 0 and curSlope == 0) or\
               (prevSlope < 0 and curSlope >= 0):
                candies += self.cnt(up) + self.cnt(dwn) + max(up, dwn)
                up, dwn = 0, 0

            if curSlope > 0:
                up += 1
            elif curSlope < 0:
                dwn += 1
            else:
                candies += 1

            prevSlope = curSlope

        candies += self.cnt(up) + self.cnt(dwn) + max(up, dwn) + 1

        return candies
        # print(candies)






test = Solution()
test.candy([1,0,2]) # 5

test = Solution()
test.candy([1,2,2]) # 4

test = Solution()
test.candy([1,3,2,2,1]) # 7

test = Solution()
test.candy([1,2,87,87,87,2,1]) # 13
