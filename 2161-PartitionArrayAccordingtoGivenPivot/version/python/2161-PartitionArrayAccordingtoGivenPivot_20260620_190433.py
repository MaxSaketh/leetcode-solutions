# Last updated: 20/06/2026, 19:04:33
# Resubmission
1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        l = []
4        r = []
5        m = []
6        for i in nums:
7            if i < pivot:
8                l.append(i)
9            if i > pivot:
10                r.append(i)
11            if i == pivot:
12                m.append(i)
13        return l + m + r