# Last updated: 20/06/2026, 19:26:23
1import numpy as np
2class Solution:
3    def getConcatenation(self, nums: List[int]) -> List[int]:
4        return (np.tile(nums,2)).tolist()