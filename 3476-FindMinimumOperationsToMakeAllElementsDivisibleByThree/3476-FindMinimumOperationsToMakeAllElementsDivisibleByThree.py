# Last updated: 19/06/2026, 18:35:12
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0

        for i in nums:
            if i % 3 == 0:
                continue   
            ops += 1
        return ops