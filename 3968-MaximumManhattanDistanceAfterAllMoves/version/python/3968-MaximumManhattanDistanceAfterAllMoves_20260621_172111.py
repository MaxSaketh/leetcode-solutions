# Last updated: 21/06/2026, 17:21:11
1class Solution:
2    def maxDistance(self, moves: str) -> int:
3    
4        cords = [0, 0]
5        for i in moves:
6            if i == "U":
7                cords[1] += 1
8            elif i == "D":
9                cords[1] -= 1
10            elif i == "L":
11                cords[0] -= 1
12            elif i == "R":
13                cords[0] += 1
14        m = moves.count('_')
15
16        return abs(cords[0]) + abs(cords[1]) + m