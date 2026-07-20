# Last updated: 20/07/2026, 20:43:37
1import math
2class Solution:
3    def findClosest(self, x: int, y: int, z: int) -> int:
4        xz = math.fabs(z-x)
5        yz = math.fabs(z-y)
6
7        if xz == yz:
8            return 0
9        elif xz < yz:
10            return 1
11        else:
12            return 2