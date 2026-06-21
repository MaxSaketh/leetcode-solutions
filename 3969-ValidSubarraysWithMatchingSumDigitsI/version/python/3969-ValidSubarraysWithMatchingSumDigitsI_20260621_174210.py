# Last updated: 21/06/2026, 17:42:10
1class Solution:
2    def countValidSubarrays(self, nums: list[int], x: int) -> int:
3        sol = 0
4        for i in range(len(nums)):
5            subsol = 0
6            for j in range(i, len(nums)):
7                subsol += nums[j]
8                if str(subsol)[0] == str(x) and str(subsol)[-1] == str(x):
9                    sol += 1
10        return sol
11                