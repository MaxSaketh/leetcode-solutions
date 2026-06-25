# Last updated: 25/06/2026, 19:12:14
1class Solution:
2    def alternatingSum(self, nums: List[int]) -> int:
3        return sum(nums[0::2]) - sum(nums[1::2])