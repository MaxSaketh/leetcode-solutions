# Last updated: 19/06/2026, 19:46:54
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = set(nums)
        nums.sort()
                
