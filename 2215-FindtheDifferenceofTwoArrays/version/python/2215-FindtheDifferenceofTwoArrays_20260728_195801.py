# Last updated: 28/07/2026, 19:58:01
1class Solution:
2    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
3        s1 = set(nums1)
4        s2 = set(nums2)
5
6        return [list(s1 - s2), list(s2 - s1)]
7