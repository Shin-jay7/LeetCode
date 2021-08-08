from __future__ import annotations


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt, ans = {}, []

        for n in nums:
            if n in cnt:
                cnt[n] += 1
            else:
                cnt[n] = 1

        for n in cnt:
            if cnt[n] > len(nums)//3:
                ans.append(n)

        return ans
        # print(ans)


test = Solution()
test.majorityElement([3,2,3]) # 3

test = Solution()
test.majorityElement([1]) # 1

test = Solution()
test.majorityElement([1,2]) # 1,2
