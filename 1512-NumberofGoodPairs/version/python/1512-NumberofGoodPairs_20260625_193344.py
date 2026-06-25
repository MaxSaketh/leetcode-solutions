# Last updated: 25/06/2026, 19:33:44
1class Solution:
2    def numIdenticalPairs(self, nums: List[int]) -> int:
3        ans = 0
4
5        for i in range(len(nums)):
6            for j in range(i+1,len(nums)):
7                if nums[i] == nums [j] and i < j:
8                    ans += 1
9        return ans