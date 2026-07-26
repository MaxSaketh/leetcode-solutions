# Last updated: 26/07/2026, 20:19:01
1import math
2class Solution:
3    def differenceOfSum(self, nums: List[int]) -> int:
4        x = sum(nums)
5        y = 0
6        for i in nums:
7            for j in str(i):
8                y += int(j)
9        return int(math.fabs(x - y))