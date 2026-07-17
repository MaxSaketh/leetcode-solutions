# Last updated: 17/07/2026, 21:52:52
1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        c = [0] * len(nums)
4        for i in range(len(nums)):
5            for j in nums:
6                if nums[i] > j:
7                    c[i] += 1
8        return c