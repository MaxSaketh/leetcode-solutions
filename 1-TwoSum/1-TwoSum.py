# Last updated: 19/06/2026, 18:56:23
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indi, i in enumerate(nums):
            for indj, j in enumerate(nums):
                if i + j == target and indi != indj:
                    return [indi, indj]

                    