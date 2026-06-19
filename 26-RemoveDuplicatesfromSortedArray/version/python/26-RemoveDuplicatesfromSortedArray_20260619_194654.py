# Last updated: 19/06/2026, 19:46:54
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        nums[:] = set(nums)
4        nums.sort()
5                