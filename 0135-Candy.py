from __future__ import annotations

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n
        flag = True

        while flag:
            flag = False
            for i in range(n):
                if i > 0 and\
                   ratings[i] > ratings[i-1] and\
                   candies[i] <= candies[i-1]:
                    candies[i] = candies[i-1]+1
                    flag = True
                if i < n-1 and\
                   ratings[i] > ratings[i+1] and\
                   candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1]+1
                    flag = True


        return sum(candies)
        # print(sum(candies))


test = Solution()
test.candy([1,0,2]) # 5

test = Solution()
test.candy([1,2,2]) # 4

test = Solution()
test.candy([1,3,2,2,1]) # 7

test = Solution()
test.candy([1,2,87,87,87,2,1]) # 13
