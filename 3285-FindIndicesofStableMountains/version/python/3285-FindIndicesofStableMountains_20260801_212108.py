# Last updated: 01/08/2026, 21:21:08
1class Solution:
2    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
3        c = []
4        for i in range(1,len(height)):
5            if height[i-1] > threshold:
6                c.append(i)
7
8        return c