# Last updated: 16/07/2026, 18:42:28
1class Solution:
2    def countPairs(self, nums: List[int], target: int) -> int:
3        count = 0
4        
5        for i in range(len(nums)):
6            for j in nums[i+1::]:
7                if nums[i] + j < target:
8                    count += 1
9
10        return count