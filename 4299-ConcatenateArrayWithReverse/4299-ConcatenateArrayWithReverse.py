# Last updated: 19/06/2026, 18:35:06
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]