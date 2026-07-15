# Last updated: 15/07/2026, 16:45:44
1import bisect
2class Solution:
3    def searchInsert(self, nums: List[int], target: int) -> int:
4        return bisect.bisect_left(nums, target)
5